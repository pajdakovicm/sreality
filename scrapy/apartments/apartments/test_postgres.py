import json as simplejson
from psycopg2.extras import Json

dict = {'name:': 'Prodej bytu 3+kk 94\xa0m²',
        'image:': [{'href': 'https://d18-a.sdn.cz/d_18/c_img_QN_Js/XeCJCa.jpeg?fl=res,400,300,3|shr,,20|jpg,90'},
                   {'href': 'https://d18-a.sdn.cz/d_18/c_img_gY_n/2KLIuG.jpeg?fl=res,400,300,3|shr,,20|jpg,90'},
                   {'href': 'https://d18-a.sdn.cz/d_18/c_img_QN_Js/bm2F4w.jpeg?fl=res,400,300,3|shr,,20|jpg,90'},
                   {'href': 'https://d18-a.sdn.cz/d_18/c_img_gY_n/skFPFT.jpeg?fl=res,400,300,3|shr,,20|jpg,90'},
                   {'href': 'https://d18-a.sdn.cz/d_18/c_img_QM_KP/s3NFzV.jpeg?fl=res,400,300,3|shr,,20|jpg,90'},
                   {'href': 'https://d18-a.sdn.cz/d_18/c_img_gU_m/Xe6BG0F.jpeg?fl=res,400,300,3|shr,,20|jpg,90'}]}

hej = [(1, 2), (3, 1)]
new_hej = []


def tuples_to_list(tup):
    arr = []
    for item in tup:
        for i in range(2):
            arr.append(item[i])
    return arr


if __name__ == '__main__':
    # print( [Json(dict, dumps=simplejson.dumps)])
    print(tuples_to_list(hej))
