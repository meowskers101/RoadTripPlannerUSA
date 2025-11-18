#NEED TO INSTALL STREAMLIT 
#USE A VIRTUAL ENVIRONMENT TO INSTALL AND RUN THE CODE
#NEED THE OTHER PYTHON FILE TO USE ITS DICTIONARIES
import streamlit as st
from collections import deque
from usstates import usa_map, state_info, state_coords
import math
import matplotlib.pyplot as plt
import json
import os
import googlemaps
from datetime import datetime
x= st.sidebar.text_input("Enter Your Google Maps API Key Here")
# Replace 'YOUR_API_KEY' with the actual key you obtained
gmaps = googlemaps.Client(key=x)
# Try to import interactive map libraries; if unavailable we'll fall back to matplotlib
try:
    import pandas as pd
    import pydeck as pdk
    _HAS_PYDECK = True
except Exception:
    _HAS_PYDECK = False

# Graph alias
graph = gmap
def get_route_info(origin, destination):
    # Request directions via public transit
    # You may change the mode to 'driving' or 'walking'
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode="driving",
                                         departure_time=now)

    if directions_result:
        # Extract the relevant details from the first route option
        leg = directions_result[0]['legs'][0]
        distance = leg['distance']['text']
        duration = leg['duration']['text']
        return distance, duration
    else:
        return "N/A", "N/A"

# Example of how you would call it:
# distance, duration = get_route_info("London, UK", "Paris, France")
# Coordinates are imported from `usstates.state_coords` so the data is shared across modules.

def plot_map(usa_graph, coords, route=None, show_edges=True, show_labels=True, geojson=None):
    """Create a matplotlib figure plotting states (from coords) and adjacency lines.
    route: ordered list of state names to highlight as the route (drawn in red).
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw state polygons (if geojson provided)
    if geojson:
        try:
            from matplotlib.patches import Polygon as MplPolygon
            for feature in geojson.get("features", []):
                geom = feature.get("geometry", {})
                coords_list = []
                if geom.get("type") == "Polygon":
                    coords_list = [geom.get("coordinates", [])]
                elif geom.get("type") == "MultiPolygon":
                    coords_list = geom.get("coordinates", [])

                for poly in coords_list:
                    # poly is a list of rings; take the exterior ring (first)
                    if not poly:
                        continue
                    exterior = poly[0]
                    # exterior is list of [lon, lat]
                    xy = [(pt[0], pt[1]) for pt in exterior]
                    patch = MplPolygon(xy, closed=True, facecolor='none', edgecolor='gray', linewidth=0.6, zorder=0)
                    ax.add_patch(patch)
        except Exception:
            # If polygon drawing fails, continue to edges fallback
            pass

    # Draw adjacency edges (light gray)
    edges_drawn = set()
    for s, neighbors in usa_graph.items():
        if s not in coords:
            continue
        for n in neighbors:
            if n not in coords:
                continue
            key = tuple(sorted((s, n)))
            if key in edges_drawn:
                continue
            edges_drawn.add(key)
            if show_edges:
                lat1, lon1 = coords[s]
                lat2, lon2 = coords[n]
                ax.plot([lon1, lon2], [lat1, lat2], color='lightgray', linewidth=0.7, zorder=1)

    # Draw points
    xs = []
    ys = []
    labels = []
    for state, (lat, lon) in coords.items():
        xs.append(lon)
        ys.append(lat)
        labels.append(state)

    ax.scatter(xs, ys, s=20, c='navy', zorder=2)

    # Labels
    if show_labels:
        for label, x, y in zip(labels, xs, ys):
            ax.text(x + 0.3, y + 0.06, label, fontsize=7, zorder=3)

    # If a route is provided, draw it in red connecting the states in order
    if route:
        route_coords = [coords[s] for s in route if s in coords]
        if len(route_coords) >= 2:
            lats = [c[0] for c in route_coords]
            lons = [c[1] for c in route_coords]
            ax.plot(lons, lats, color='red', linewidth=2.5, zorder=4)
            ax.scatter(lons, lats, s=40, c='red', zorder=5)

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('USA States (approx) and adjacencies')
    ax.set_aspect('equal', adjustable='datalim')
    ax.grid(True, linestyle=':', linewidth=0.5)
    return fig


def show_interactive_map(usa_graph, coords, route=None, show_edges=True, show_labels=True, geojson=None):
    """Use pydeck to show an interactive map with points, adjacency lines, and an optional route.
    Falls back to matplotlib if pydeck/pandas are not available.
    """
    if not _HAS_PYDECK:
        # fallback
        return None

    # Prepare points dataframe
    rows = []
    for name, (lat, lon) in coords.items():
        rows.append({"name": name, "lat": lat, "lon": lon})
    points = pd.DataFrame(rows)

    # Edges
    edges = []
    edges_seen = set()
    for s, neighbors in usa_graph.items():
        if s not in coords:
            continue
        for n in neighbors:
            if n not in coords:
                continue
            key = tuple(sorted((s, n)))
            if key in edges_seen:
                continue
            edges_seen.add(key)
            lat1, lon1 = coords[s]
            lat2, lon2 = coords[n]
            edges.append({"start": [lon1, lat1], "end": [lon2, lat2]})

    layers = []

    # If a GeoJSON file was provided, add it as a GeoJsonLayer under the points
    if geojson:
        try:
            geo_layer = pdk.Layer(
                "GeoJsonLayer",
                data=geojson,
                stroked=True,
                filled=False,
                get_line_color=[160, 160, 160],
                line_width_min_pixels=1,
                pickable=False,
            )
            layers.append(geo_layer)
        except Exception:
            pass

    # Scatter layer for states
    scatter = pdk.Layer(
        "ScatterplotLayer",
        data=points,
        get_position='[lon, lat]',
        get_fill_color=[10, 30, 160],
        get_radius=25000,
        pickable=True,
        auto_highlight=True,
    )
    layers.append(scatter)

    # Text labels (optional)
    if show_labels:
        text_layer = pdk.Layer(
            "TextLayer",
            data=points,
            get_position='[lon, lat]',
            get_text='name',
            get_size=14,
            get_color=[0, 0, 0],
            get_alignment_baseline='bottom',
            pickable=False,
        )
        layers.append(text_layer)

    # Line layer for adjacencies
    if show_edges and edges:
        line_layer = pdk.Layer(
            "LineLayer",
            data=edges,
            get_source_position="start",
            get_target_position="end",
            get_width=1,
            get_color=[200, 200, 200],
            pickable=False,
        )
        layers.append(line_layer)

    # Route overlay as a PathLayer
    if route:
        path = []
        for s in route:
            if s in coords:
                lat, lon = coords[s]
                path.append([lon, lat])
        if len(path) >= 2:
            path_layer = pdk.Layer(
                "PathLayer",
                data=[{"path": path}],
                get_path="path",
                get_color=[240, 50, 50],
                width_scale=20,
                width_min_pixels=3,
            )
            layers.append(path_layer)

    # View centered on continental US
    view_state = pdk.ViewState(latitude=39.5, longitude=-98.35, zoom=3.5)

    # Add a simple tooltip showing the state name
    deck = pdk.Deck(layers=layers, initial_view_state=view_state, tooltip={"text": "{name}"})
    return deck

def BFS_v1(graph, start, goal):
    queue = deque([start]) #my to do list starts with the start node
    while queue: #while I can still go to some node in the queue
        current_node = queue.popleft() #popleft gets the first node in the queue, FIFO
        print(current_node)
        if current_node == goal:
            print("I found the goal!")
            return
        
        #append all the neighbor nodes to the queue
        for node in graph[current_node]:
            queue.append(node)
    
    print("I cannot find the goal!")
    return

# ----- BFS Function -----
def bfs_path(graph, start, goal):
    queue = deque([start])
    visited = set()
    parent = {}

    while queue:
        current = queue.popleft()
        visited.add(current)

        if current == goal:
            # reconstruct path
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = current
    return None


st.title("USA RoadTrip Planner!")
st.write("This app helps you find the fastest way to get to state to another state!")
states = sorted(list(usa_map.keys()))
start_state = st.selectbox("Start States", states)
end_state = st.selectbox("End States", states)
must_visit = st.multiselect("Input your must select states!(In order)", states)
# Map display controls
show_map = st.checkbox("Show map of USA (points & adjacencies)")
show_edges = st.checkbox("Show adjacency edges", value=True)
# Default to showing labels so state names are visible
show_labels = st.checkbox("Show state labels", value=True)

# Attempt to load a GeoJSON file named 'usstates.geojson' in the same folder to draw state borders
geojson = None
geojson_path = os.path.join(os.path.dirname(__file__), 'usstates.geojson')
if os.path.exists(geojson_path):
    try:
        with open(geojson_path, 'r', encoding='utf-8') as f:
            geojson = json.load(f)
        st.info("Loaded 'usstates.geojson' — state borders will be shown on the map.")
    except Exception as e:
        st.warning(f"Found 'usstates.geojson' but failed to load it: {e}")
else:
    st.info("No 'usstates.geojson' found — state borders disabled. Place a GeoJSON file named 'usstates.geojson' beside this script to enable borders.")

# Prepare a BFS_path variable for later plotting
BFS_path = None
#ios is "Info of States"

x=0
y=0
z=y
if st.button("Find Shortest Path"):
    if start_state == end_state:
        st.warning("The destinations are the same...") 

    else:
        # Build the full route robustly: start -> (must_visit...) -> end
        route_points = list(must_visit) + [end_state]
        prev = start_state
        full_path = []
        path_not_found = False

        for target in route_points:
            subpath = bfs_path(usa_map, prev, target)
            if subpath is None:
                path_not_found = True
                break
            if not full_path:
                full_path.extend(subpath)
            else:
                # avoid duplicating the connecting node
                full_path.extend(subpath[1:])
            prev = target

        BFS_path = None if path_not_found else full_path


    if BFS_path == None:
        st.error("Path not found!")
    else:
        st.write("""➡️""".join(BFS_path))
        st.success("Path Found!")
        st.write()

        # Simple route summary
        visited_states = BFS_path
        total_stops = len(visited_states)
        total_drive = sum((state_info.get(s, {}).get("drive_time", 0) or 0) for s in visited_states)
        must_in_route = [s for s in must_visit if s in visited_states]

        st.subheader("Route summary")
        st.write(f"Stops on route: {total_stops}")
        st.write(f"Estimated total drive time (hrs): {total_drive}")
        if must_in_route:
            st.write(f"Must-visit on route: {', '.join(must_in_route)}")
        else:
            st.write("No must-visit states are on the computed route.")

        # Show info expanders for each state visited on the trip (must-visit marked)
        # Prepare a case-insensitive lookup so small naming differences won't hide info
        info_lookup = {k.lower(): v for k, v in state_info.items()}
        available_info_states = sorted(state_info.keys())
        if available_info_states:
            st.write(f"States with info available: {', '.join(available_info_states)}")

        for state in visited_states:
            title = f"⭐ {state}" if state in must_visit else state
            # try exact key first, then case-insensitive match
            info = state_info.get(state) or info_lookup.get(state.lower())
            with st.expander(title):
                if not info:
                    st.write("No info available for this state.")
                    continue
                things = info.get("things_to_do", [])
                if things:
                    st.write("Things to do:")
                    for t in things:
                        st.write(f"- {t}")
                fun = info.get("fun_fact")
                if fun:
                    st.write("Fun fact:")
                    st.write(fun)
                drive = info.get("drive_time")
                if drive is not None:
                    st.write("Drive time (hrs):", drive)

        # Show the map (graph) and overlay the route if requested
        if show_map:
            try:
                deck = show_interactive_map(graph, state_coords, route=visited_states, show_edges=show_edges, show_labels=show_labels)
                if deck is not None:
                    st.pydeck_chart(deck)
                else:
                    fig = plot_map(graph, state_coords, route=visited_states, show_edges=show_edges, show_labels=show_labels)
                    st.pyplot(fig)
            except Exception as e:
                st.error(f"Error drawing map: {e}")

# If user wants to just preview the map without computing a route
if show_map and BFS_path is None:
    try:
        deck = show_interactive_map(graph, state_coords, route=None, show_edges=show_edges, show_labels=show_labels)
        if deck is not None:
            st.pydeck_chart(deck)
        else:
            fig = plot_map(graph, state_coords, route=None, show_edges=show_edges, show_labels=show_labels)
            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error drawing map preview: {e}")



