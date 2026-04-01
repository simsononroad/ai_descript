from google import genai



def generate_from_repo(repo: str, api_key_file: str, output_file=False, output_file_name="markdown.md", *args, **kwarg):
    GEMINI_API_KEY = ""
    with open(api_key_file, "r") as f:
        GEMINI_API_KEY = f.read()
    
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Csinálj ennek a repositorynak egy markdown-ban formázott leírást / használati útmutatót. Csak a nyers markdown-ban formázott szöveget írd le.: {repo}",
    )
    be_readme = False
    commit_md = False
    for key, val in kwarg.items():
        if key == "be_readme":
            if val == True:
                print("igaz")
                be_readme = True
            else:
                be_readme = False
        
        if key == "commit_md":
            if val == True:
                commit_md = True
            else:
                commit_md = False
        
    if be_readme:
        with open("readme.md", "w") as f:
            f.write(response.text)
    else:
        with open(output_file_name, "w") as f:
            f.write(response.text)

generate_from_repo(repo="https://github.com/simsononroad/masodfoku_egyenlet_megoldas", api_key_file="", be_readme=True)