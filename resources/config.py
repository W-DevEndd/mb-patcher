
class Config:
    # Absolute path to mimecraft apk file
    minecraft_apk = "./files/arm64-v8a/minecraft.apk"
    minecraft_apk_32 = "./files/armebi-v7a/minecraft.apk"

    # (Optinal) Absolute path to Material bin loader lib.so file
    mb_libso = ""
    mb_libso_32 = ""

    make_for_32 = False

    force_unlock_visual = True