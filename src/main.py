import pandas as pd
import requests
from pandas import DataFrame

filename = '../sheet/test-urls.xlsx'
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 ("
                        "KHTML, like Gecko) Version/15.3 Safari/605.1.15"}


def validate_url(check_url: str) -> str:
    """
    This function validate if the URL is valid and returns a successful return code
    :param check_url:
    :return: str 'Good' or 'Bad'
    """
    try:
        response = requests.get(check_url, headers=header, timeout=3)
        if response.status_code == 200:
            print(
                f'{check_url} Response Status Code: {response.status_code} Connection Status: Good')
            return 'Good'
        print(f'{check_url} Status Code: {response.status_code} Connection Status: Bad')
    except Exception as e:
        print(f'{check_url} Status Code: Exception Connection Status: Bad')
    return 'Bad'


def generate_connection_stats(excel_df) -> DataFrame:
    """
    This function takes the DataFrame from Excel file, filters the columns with name 'URL',
    validates the urls, adds it to the DataFrame and returns the DataFrame
    :param excel_df:
    :return: DataFrame with Status column
    """
    connection_stats = list()
    url_cols_list = list()
    excel_cols = excel_df.keys().values
    for col in excel_cols:
        if 'url' in col.lower():
            url_cols_list.append(col)
    if len(url_cols_list) > 0:
        print(f'\nFetching data for columns: {url_cols_list}')
        url_df = pd.DataFrame(df.loc[:, url_cols_list])
        url_val_list = url_df.values.tolist()
        for urls in url_val_list:
            for url in urls:
                connection_stats.append(validate_url(url))
    else:
        print('No columns containing URL found. Quiting program.')
    excel_df["Status"] = connection_stats
    print('\n\nUpdated DataFrame')
    print(f'{excel_df}')
    return excel_df


def write_to_excel(new_df):
    """
    This function writes the provided DataFrame to the current Excel file in the new sheet as
    'URL Status'
    :param new_df:
    :return: void
    """
    with pd.ExcelWriter(filename, mode='a', if_sheet_exists="replace") as writer:
        new_df.to_excel(writer, sheet_name='URL Status', index=False)


if __name__ == "__main__":
    print('Starting with URL Validator')
    df = pd.read_excel(filename, sheet_name='Sheet1')
    print('Excel file contents: ')
    print(df)
    write_to_excel(generate_connection_stats(df))
