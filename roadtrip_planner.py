#NEED TO INSTALL STREAMLIT 
#USE A VIRTUAL ENVIRONMENT TO INSTALL AND RUN THE CODE
#NEED THE OTHER PYTHON FILE TO USE ITS DICTIONARIES
import streamlit as st
from collections import deque
from usstates import usa_map
from usstates import state_info
import math
graph = usa_map

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

