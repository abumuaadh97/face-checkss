mkdir -p ~/streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCCRS = false\n\
\n\
" > ~/.streamlit/config.toml