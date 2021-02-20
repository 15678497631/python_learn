print("Hello ! pyhton.")


def check_dict_get_default():
    _dict_ = {'point': "123", 'point_0': "123", 'point_1': "123"}
    print(_dict_.get("point_12","0"))


if __name__ == "__main__":
    check_dict_get_default()