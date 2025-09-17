@app.get("/extension/{ext}")
def extension_info(ext: str):
    # Freemium: devuelve descripción básica
    info = get_extension_info(ext)
    if "description" in info and len(info["description"]) > 200:
        # Descripción a 200 caracteres
        info["description"] = info["description"][:200] + "..."
    return info
