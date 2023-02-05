from utils.transfermarkt import get_transfers_by_date
from datetime import datetime, timedelta
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_yesterday_transfers(*args, **kwargs):
    """
    code for loading yesterday transfermarkt transfers data from the webpage.

    Returns:
        DataFrame
    """
    # Specify your data loading logic here
    yesterday = datetime.now() - timedelta(days=1)
    transfers = get_transfers_by_date(yesterday.strftime('%Y-%m-%d'))

    df = DataFrame(transfers)

    return df


@test
def test_output(df, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
