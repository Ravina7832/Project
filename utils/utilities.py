import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(message)s', level=logging.INFO)


def checkEqual(from_json, from_api):
    is_equal = len(from_json) == len(from_api) and sorted(from_json) == sorted(from_api)
    if not is_equal:
        device_in_json_but_not_in_api = [device for device in from_json if device not in from_api]
        device_in_api_but_not_in_json = [device for device in from_api if device not in from_json]
        device_in_json_but_not_in_api_msg = f'{", ".join(device_in_json_but_not_in_api)} {"are" if len(device_in_json_but_not_in_api) > 1 else "is"} in JSON but not found in API response.' if device_in_json_but_not_in_api else ""
        device_in_api_but_not_in_json_msg = f'{", ".join(device_in_api_but_not_in_json)} {"are" if len(device_in_api_but_not_in_json) > 1 else "is"} in API response but not found in JSON.' if device_in_api_but_not_in_json else ""
        raise AssertionError(f"{device_in_json_but_not_in_api_msg} {device_in_api_but_not_in_json_msg}")
    logger.info(f"{', '.join(from_api)} are available in API Response and JSON.")
    return True


def checkEqual_json(first_json, second_json, raise_error=True):
    is_equal = len(first_json) == len(second_json) and sorted(first_json) == sorted(second_json)
    if not is_equal:
        devices_in_first_json_but_not_in_second = [device for device in first_json if device not in second_json]
        devices_in_second_json_but_not_in_first = [device for device in second_json if device not in first_json]
        device_in_json_but_not_in_api_msg = f'{", ".join(devices_in_first_json_but_not_in_second)} {"are" if len(devices_in_first_json_but_not_in_second) > 1 else "is"} in Old JSON but not found in New Json.' if devices_in_first_json_but_not_in_second else ""
        device_in_api_but_not_in_json_msg = f'and {", ".join(devices_in_second_json_but_not_in_first)} {"are" if len(devices_in_second_json_but_not_in_first) > 1 else "is"} in New json but not found in Old Json.' if devices_in_second_json_but_not_in_first else ""
        if raise_error:
            raise AssertionError(f"{device_in_json_but_not_in_api_msg} {device_in_api_but_not_in_json_msg}")
        return False
    return True


def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        try:
            float(n)
            return True
        except ValueError:
            pass
    return False
