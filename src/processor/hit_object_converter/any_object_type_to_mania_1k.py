from typing import cast

from custom_types import HitObject, ManiaHitObject, TaikoHitObject


def any_object_type_to_mania_1k(hit_object: ManiaHitObject | HitObject | TaikoHitObject) -> ManiaHitObject:
    """将滑条，转盘转换为长条，其他的不用转换\n
    把物件添加到 mania 一轨

    Args:
        hit_object (ManiaHitObject | HitObject): 转换前物件的信息

    Returns:
        ManiaHitObject: 转换后物件的信息
    """
    if hit_object["type"] in ("kat", "large kat", "don", "large don"):
        hit_object["type"] = "hit circle"
    if hit_object["type"] in ("slider", "spinner", "drum roll", "denden note"):
        hit_object["type"] = "hold"

    mania_hit_object = cast(ManiaHitObject, hit_object)
    mania_hit_object.update({"key": 1})

    return mania_hit_object
