from janome import sysdic
from janome.dic import UserDictionary
from janome.progress import SimpleProgressIndicator


def main(csv_dict_path: str, output_dict_path: str):
    user_dict = UserDictionary(
        csv_dict_path,
        "utf8",
        "simpledic",
        sysdic.connections,
        progress_handler=SimpleProgressIndicator(update_frequency=0.01),
    )
    user_dict.save(output_dict_path)


if __name__ == "__main__":
    csv_dict_path: str = "scripts/files/user_dictionary.csv"
    output_dict_path: str = "apps/tmp/userdic"
    main(csv_dict_path, output_dict_path)
