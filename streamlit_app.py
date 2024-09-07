import streamlit as st


st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([1,1, 2])

try:
    from yaml_digest import meal_info
except:
    print('LOL')
    " Error encountered in meal processor "
    st.stop()

def show_reciepe(arg ):
    st.session_state["txtarea"] = str(meal_info[arg])
    




meal_names = [ i['dish'] for i in meal_info]
with col1:
    " # Browse meals"
    st.text_input(label = "filter", value  = "",  key = "search" )
    
    flt_text = st.session_state["search"]
    
    for idx, i in enumerate(meal_names):
        if flt_text.lower() in i.lower():
            st.button(str(i) , on_click = lambda: show_reciepe(idx)  )

with col2:
    st.text_input(label = "filter reciepe details", value  = "",  key = "search2" )
    txt = st.text_area(
                        label = "Recipe Details",
                        key = "txtarea",
                        value = "",
                        height = 700,
                        )

    
