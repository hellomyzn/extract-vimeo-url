import json

def extract_vimeo_url(path):
    # retrieve chunks including 720p
    txt_file = path
    txt_data = []

    with open(txt_file, mode="r") as f:
        for line in f:
            if "720p" in line:
                txt_data.append(line)

    # retrieve json data
    target = " = "
    idx = txt_data[0].find(target)
    json_response = txt_data[0][idx+len(target):]

    # retrieve url from json data
    json_load = json.loads(json_response)
    print(json_load['request']['files']['progressive'][1]['url'])

if __name__ == '__main__':
    import sys
    args = sys.argv
    extract_vimeo_url(args[1])