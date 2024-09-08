import streamlit as st


st.set_page_config(layout="wide")


try:
    from yaml_digest import meal_info
except :
    " Error encountered in meal processor "
    st.stop()
    raise SystemExit()

def show_reciepe():
    for i in rendered_buttons:
        if ( st.session_state[i] == True):
            break
    idx = int(i[6:])
    st.session_state["txtarea"] = str(meal_info[idx])
    
rendered_buttons = []
col1, col2, col3 = st.columns([1,1, 2])

meal_names = [ i['dish'] for i in meal_info]
with col1:
    " # Browse meals"
    st.text_input(label = "filter dishes by name", value  = "",  key = "search" )
    flt_text = st.session_state["search"]
    for idx, i in enumerate(meal_names):
        if flt_text.lower() in i.lower():
            rendered_buttons.append ('button'+str(idx))
            st.button(str(i) ,key = 'button'+str(idx),on_click = show_reciepe   )
            # on_click = lambda: show_reciepe(idx) -- it didn't work

with col2:
    st.text_input(label = "filter reciepe details", value  = "",  key = "search2" )
    txt = st.text_area(
                        label = "Recipe Details",
                        key = "txtarea",
                        value = "",
                        height = 700,
                        )

