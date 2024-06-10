import streamlit as st

# JavaScript code for drag-and-drop functionality
drag_and_drop_js = """
<script>
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  var node = document.getElementById(data);
  var fieldImage = document.getElementById("field-image");
  var fieldRect = fieldImage.getBoundingClientRect();
  var offsetX = ev.clientX - fieldRect.left;
  var offsetY = ev.clientY - fieldRect.top;
  node.style.position = "absolute";
  node.style.left = offsetX + "px";
  node.style.top = offsetY + "px";
  fieldImage.appendChild(node);
}

function dragOver(ev) {
  ev.preventDefault();
}
</script>
"""

teams = {
    "Team Apurba": {
        "Apurba": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Unpredictable leg breaks"}, 
        "Arefin": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Pace"},
        "Moid": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Full toss"},
        "Rahman": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Off spin, ball drops out side leg stick"},
        "Tanvir": {"Strong Point": "Fielding", "Weak Point": "Bowling", "Note": "Left handed; Bowls good length mid stick"},
        "Kaiser": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Ball bounces; Ball spins faster after bounce; high off break "},
        "Amit": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Unpredictable swings"},
        "Jilani": {"Strong Point": "Not enough data", "Weak Point": "Not enough data", "Note": "Misfields"}
    },
    "Team Mushuk": {
        "Mishuk": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Good length balls"},
        "Rafi": {"Strong Point": "Not enough data", "Weak Point": "Fielding", "Note": "Misfields"},
        "Limon": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Overconfident and capricious in the field"},
        "Miftah": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Comparative soft hitter; good length slow mid stick balls"},
        "Kader": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Throws are near accurate"},
        "Saikat": {"Strong Point": "Batting, Fielding", "Weak Point": "Bowling", "Note": "Fields well; short length mid stick balls"},
        "Saddam": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Easy to manipulate, pace"},
        "Rahat": {"Strong Point": "Bowling", "Weak Point": "Batting", "Note": "Misfields; slow goodlength soft swing balls"}
    },
    "SXI": {
        "Zazi": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Wide checks and less experiments"},
        "Safi": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Wide checks and less experiments, oversteps"},
        "Ayaz": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Pace; good on singles"},
        "Jhalak": {"Strong Point": "Batting", "Weak Point": "Bowling", "Note": "Caution in front foot shots and timing, monotonous swings"},
        "Imran": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Ball bounces"},
        "Ashfaque": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Pace, caution in timing and hitting"},
        "Raju": {"Strong Point": "Batting, Fielding", "Weak Point": "Bowling", "Note": "Tries playing cross bat"},
        "Meraz": {"Strong Point": "Batting, Bowling", "Weak Point": "Bowling", "Note": "Caution playing mid and off-stick balls"}
    }
}

def main():
    st.title("Eid Tournament Game Plan Strategy")
    st.markdown("**by Jhalak**", unsafe_allow_html=True)

    # Add custom CSS to reduce the space between title and subtitle
    st.markdown(
        """
        <style>
        .css-1u3imnb { margin-bottom: -0.5rem; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display navigation options
    page = st.sidebar.selectbox("Navigate", ["SW Data", "Field Plan"])

    if page == "SW Data":
        render_player_list()
    elif page == "Field Plan":
        render_field()

def render_player_list():
    # Display team selection
    selected_team = st.selectbox("Select Team", ["Team Apurba", "Team Mushuk", "SXI"])

    # Render players for selected team
    render_players(selected_team)

def render_players(team):
    st.write(f"### Players for {team}:")
    players = get_players_data(team)

    # Render each player as clickable with info
    for player, traits in players.items():
        if st.button(player):
            show_player_details(player, traits)

def show_player_details(player, traits):
    st.write(f"## {player}")
    st.markdown(f"**Strong Point:** <span style='color:green'>{traits['Strong Point']}</span>", unsafe_allow_html=True)
    st.markdown(f"**Weak Point:** <span style='color:red'>{traits['Weak Point']}</span>", unsafe_allow_html=True)
    st.markdown(f"**Note:** _{traits['Note']}_", unsafe_allow_html=True)

def render_field():
    # Load and display field image
    field_image = "sc.png"  # Replace "your_field_image.png" with the path to your field image
    st.image(field_image, use_column_width=True, output_format="PNG")

    # Add JavaScript code for drag-and-drop functionality
    st.markdown(drag_and_drop_js, unsafe_allow_html=True)

    # Display draggable player list
    st.sidebar.header("Draggable Players")
    selected_team = st.selectbox("Select Team", ["Team Apurba", "Team Mushuk", "SXI"])
    players = get_players_data(selected_team)
    for player in players:
        st.sidebar.markdown(f"<div id='{player}' draggable='true' ondragstart='drag(event)'>{player}</div>", unsafe_allow_html=True)

# Retrieve players data
def get_players_data(team):
    return teams[team]

# Run the app
if __name__ == "__main__":
    main()
