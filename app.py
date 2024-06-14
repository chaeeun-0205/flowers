import streamlit as st


page_title="꽃 도감",
page_icon="./images/flower.png"


st.markdown("""
<style>
img { 
    max-height: 300px;
}
.streamlit-expanderContent div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.streamlit-expanderHeader {
    pointer-events: none;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


st.title("streamlit 꽃 도감")
st.markdown("**꽃**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "빨강": "🟥",
    "주황": "🟧",
    "노랑": "🟨",
    "초록": "🟩",
    "파랑": "🟦",
    "하양": "⬜",
    "보라": "🟪",
    
}

initial_flowers = [
    {
        "name": "해바라기",
        "types": ["노랑"],
        "image_url": "https://i.namu.wiki/i/bWUWcpdS9bxlsyY7rRqX5xAzi2FAAMnHx5G4i7dmW08bnkhm7kzwnnZBlDATgBu9wTPDmvN4yFqn8Vnfp4a_41KViGomTHXkNhqkUPj379_BtcdnhN6ICxPq0Ejz5MJJgBtwXKNP7l8q1wlWgtlP6A.webp",
    },
    {
        "name": "튤립",
        "types": ["빨강"],
        "image_url": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fpng.pngtree.com%2Fthumb_back%2Ffw800%2Fbackground%2F20210330%2Fpngtree-spring-stepping-bouquet-red-tulips-image_597359.jpg&type=sc960_832"},
    {
        "name": "마리골드",
        "types": ["주황"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA3MTFfNiAg%2FMDAxNjg5MDUzMDE3OTk4.pu6I451BmCavPkPu4IZUSNw_i5_KHhoGuRgSisv2DhQg.wJzeVRM8DgyWVqx3eKPdEaSlRIoUymrhyfUrtYMSxYQg.JPEG.optuspharm%2Fshutterstock_1509180620.jpg&type=sc960_832",
    },
    {
        "name": "네잎클로버",
        "types": ["초록"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA1MjRfMjc1%2FMDAxNzE2NTM4MTE1MDc5.RXcoAECiWU_W04UFGbSMeRYzj45WW5YEfG2V_qwuvPAg.OaJUxUxoNWxbsbutrJq3bKfGVbOks0leUQgtMuE16v4g.JPEG%2F20240520%25A3%25DF105449.jpg&type=sc960_832"
    },
    {
        "name": "블루데이지",
        "types": ["파랑"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDA0MTNfMjY5%2FMDAxNzEyOTg1NTIxNzg0.2CySypllADdwt7g4KipDlGQlxlU2ZAVI-pWNVwMswe8g.L0hJ-dzyV9NMKjLjlSnn7gFof5HSPC6Ig0w2uGILbOAg.JPEG%2F20240413%25A3%25DF141520.jpg&type=sc960_832"
    },
    {
        "name": "도라지꽃",
        "types": ["보라"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA3MjNfMTAw%2FMDAxNjU4NTgzMDEwOTAw.SE3-pU1nqq2NbJIZ2nKggWfgLt1r5vIiTqlCZ6FzEgMg.Psr_IrHa15oz71TnVuIkjdzV3Hlk4wkKbNbvgbYS4aIg.JPEG.actsok0001%2F20220715_070546.jpg&type=sc960_832"
    },
]

example_flowers = {
    "name": "튤립",
    "types": ["빨강"],
    "image_url": ""
}

if "flowers" not in st.session_state:
    st.session_state.flowers = initial_flowers

auto_complete = st.toggle("예시 데이터로 채우기")
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="꽃 이름",
            value=example_flowers["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="꽃 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_flowers["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="꽃 이미지 URL",
        value=example_flowers["image_url"] if auto_complete else "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fpng.pngtree.com%2Fthumb_back%2Ffw800%2Fbackground%2F20210330%2Fpngtree-spring-stepping-bouquet-red-tulips-image_597359.jpg&type=sc960_832"
    )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("꽃의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("꽃의 속성을 적어도 한개 선택해주세요.")
        else:
            st.success("꽃을 추가할 수 있습니다.")
            st.session_state.flowers.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })

for i in range(0, len(st.session_state.flowers), 3):
    row_flowers = st.session_state.flowers[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_flowers)):
        with cols[j]:
            flower = row_flowers[j]
            with st.expander(label=f"**{i+j+1}. {flower['name']}**", expanded=True):
                st.image(flower["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in flower["types"]]
                st.text(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.flowers[i+j]
                    st.rerun()
