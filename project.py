import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🪄"
)

st.title("AI Text Generator")
st.write("Enter a sentence and AI will complete it.")

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-1.5B-Instruct"
    )

generator = load_model()

prompt = st.text_area(
    "Enter your text",
    placeholder="Artificial intelligence..."
)

if st.button("Generate text"):
    if prompt.strip():
        with st.spinner("Generating..."):
            result = generator(
                prompt,
                max_new_tokens=50,
                num_return_sequences=1
            )

        generated_text = result[0]["generated_text"]

        st.subheader("Generated text")
        st.write(generated_text)

    else:
        st.warning("⚠️ Please enter some text first!")
