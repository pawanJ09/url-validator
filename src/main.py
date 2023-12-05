import pandas as pd
import requests


def validate_url(check_url: str) -> str:
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return 'Good'
    except Exception as e:
        # print(e)
        pass
    return 'Bad'


if __name__ == "__main__":
    print('Starting with URL Validator')
    df = pd.read_excel('../sheet/test-urls.xlsx', sheet_name='Sheet1')
    print('Excel file contents: ')
    print(df)
    cols = df.keys().values
    cols_list = list()
    for col in cols:
        if 'url' in col.lower():
            cols_list.append(col)
    if len(cols_list) > 0:
        print(f'\nFetching data for columns: {cols_list}')
        url_df = pd.DataFrame(df.loc[:, cols_list])
        url_list = url_df.values.tolist()
        print(f'\nURLs found: {url_list}')
        for urls in url_list:
            for url in urls:
                print(f'{url} Connection Status: {validate_url(url)}')
    else:
        print('No columns containing URL found. Quiting program.')

