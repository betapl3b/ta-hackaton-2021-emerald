import json
import os
import sys


def dict_merge(dct, merge_dct):
    """"""
    for k, v in merge_dct.items():
        if k in dct and isinstance(dct[k], dict):
            dict_merge(dct[k], merge_dct[k])
        elif k in dct and isinstance(dct[k], list):
            dct[k] = dct[k] + merge_dct[k]
        else:
            dct[k] = merge_dct[k]


def prepare_html(path):
    results = {}
    for json_file in os.listdir(path):
        inner_dict = {}
        with open(f'{path}/{json_file}', 'r') as f:
            json_content = json.loads(f.read())
            if isinstance(json_content, list):
                for feature in json_content:
                    inner_dict.update({feature['name']: feature})
            elif isinstance(json_content, dict):
                inner_dict.update({json_content['name']: json_content})
        dict_merge(results, inner_dict)

    html = ''
    test_index = 1
    for feature in results.values():
        for test in feature['elements']:
            step_id_list = []
            steps_html = ''
            summ_dur = 0
            test_status = 'passed'
            for step_index, step in enumerate(test['steps']):
                step_id = f's-{test_index}-{step_index}'
                step_id_list.append(step_id)
                steps_html += f'''<tr id="{step_id}" class="hidden"><td>{step_index}</td>
    <td colspan="3" class="step-name">{step['name']}</td><td>{step['result']['duration']}</td><td>{step['result']['status']}</td>
    </tr>'''
                summ_dur += int(step['result']['duration'])
                test_status = 'failed' if step['result']['status'] != 'passed' else test_status

            html += f'''<tr><td><button type="button" id="b{test_index}" aria-expanded="false"
    onclick="toggle(this.id,'{str(",#".join(step_id_list))}');"><svg xmlns="\http://www.w3.org/2000/svg&quot;"
    viewBox="0 0 80 80" focusable="false"><path d="M70.3 13.8L40 66.3 9.7 13.8z"></path></svg></button></td>
    <td class="test-index">{test_index}</td><td class="test-feature">{feature['name']}</td>
    <td class="test-name">{test['name']}</td><td class="test-duration">{summ_dur}</td>
    <td class="test-status">{test_status}</td></tr>{steps_html}'''
            test_index += 1

    return html


if __name__ == "__main__":
    out = prepare_html(sys.argv[1])
    print(out)
