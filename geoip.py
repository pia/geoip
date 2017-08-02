from urllib.request import urlopen
import sys, json

def query(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    rawData = urlopen(url).read()
    ''' 
    {'code': 0, 'data': {'country': '中国', 'country_id': 'CN', 'area': '华北', 'area_id': '100000', 
    'region': '北京市', 'region_id': '110000', 'city': '北京市', 'city_id': '110100', 'county': '', 'county_id': '-1', 
    'isp': '联通', 'isp_id': '100026', 'ip': '114.242.250.18'}}
    '''
    result = json.loads(rawData, encoding='utf-8')
    print(result['data']['country'] + ', ' + result['data']['region'] + ', ' + result['data']['city'] + ', ' + result['data']['isp'])

def main():
    try:
        ip = sys.argv[1]
    except IndexError:
        print('TODO 查询本机 ip')
    else:
        query(ip)

if __name__ == '__main__':
    main()