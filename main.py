import json

def extract_vimeo_url(path: str) -> str:
    # retrieve chunks including 720p
    txt_data = []

    with open(path, mode="r") as f:
        for line in f:
            if "720p" in line:
                txt_data.append(line)

    # retrieve json data
    target = " = "
    idx = txt_data[0].find(target)
    json_data = txt_data[0][idx+len(target):]

    # retrieve url from json data
    json_load = json.loads(json_data)
    videos = json_load['request']['files']['progressive']

    for v in videos:
        if v['quality'] == '720p':
            video_url_720 = v['url']
    
    return video_url_720


if __name__ == '__main__':
    import sys
    args = sys.argv
    print(extract_vimeo_url(args[1]))