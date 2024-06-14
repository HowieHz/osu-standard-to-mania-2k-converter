from custom_types import ManiaHitObject
from logger import debug


def generate_mania_2k_osu_file(
    file_metadata: list[str], hit_objects_list: list[ManiaHitObject]
) -> str:
    debug("file_metadata", data=file_metadata)
    debug("hit_objects_list", data=hit_objects_list)

    # 生成元数据
    raw_file_metadata = "".join(file_metadata)

    # 米例：256,192,83,1,0,0:0:0:0:
    # 面例：256,192,505,128,0,1347:0:0:0:0:

    # 生成 .osu 文件 [HitObjects] 这一段数据
    raw_hit_objects_list = "[HitObjects]\n"
    for hit_object in hit_objects_list:
        x = 128 if hit_object["key"] == 1 else 384
        if hit_object["type"] == "hit circle":
            # x,y,时间,物件类型,打击音效,物件参数,打击音效组（默认 0:0:0:0:）
            raw_hit_objects_list += f"{x},192,{hit_object['start_time']},1,0,0:0:0:0:\n"  # TODO 要能把打击音效和打击音效组继承过来
        elif hit_object["type"] == "hold":
            # x,y,开始时间,物件类型,长键音效,结束时间:长键音效组
            raw_hit_objects_list += f"{x},192,{hit_object['start_time']},128,0,{hit_object['end_time']}:0:0:0:0:\n"  # TODO 同上面
        else:
            pass

    # 文件末不用加空行，因为上面每行末尾都有\n，保持和制铺器生成的一致
    return raw_file_metadata + raw_hit_objects_list
