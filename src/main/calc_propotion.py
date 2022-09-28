def get_proportion(langs_bytes, lang: str, total_bytes):
    if langs_bytes:
        filtered_lang_byte = list(filter(lambda lang_byte: lang_byte[0] == lang, langs_bytes))
        byte = filtered_lang_byte[0][1]
        proportion = (byte / total_bytes) * 1000
        return proportion
    else:
        print("your languages bytes table is empty")
        return -1


def get_total_proportion(total_proportion, proportion):
    total_proportion += proportion
    return total_proportion
