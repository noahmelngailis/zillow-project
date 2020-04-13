    import pandas as pd
    import numpy as np
    from env import get_db

    def acquire(db):
    """This function uses env to connect to codeup sequel database by calling db name.
    It selects bedrooms, bathrooms, area as well as tax amount home value and fips.  From May 1 through June 30th 2017.
    It has removed data listings with 0 bathrooms or 0 bedrooms and has filtered property type as Single family residential"""

    url = get_db(db)
    sql = """SELECT bedroomcnt as bedrooms, 
    bathroomcnt as bathrooms, 
    calculatedfinishedsquarefeet as sq_feet,
    taxamount as property_tax, 
    taxvaluedollarcnt as home_value, 
    proptype.propertylandusedesc as property_type, 
    fips
    FROM properties_2017
    JOIN predictions_2017 USING (parcelid)
    JOIN propertylandusetype USING (propertylandusetypeid)
    WHERE (transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30')
    AND (propertylandusedesc = 'Single Family Residential')
    AND bedroomcnt > 0
    AND bathroomcnt > 0
    AND taxvaluedollarcnt > 0;
    """
    df = pd.read_sql(sql, url)
    return df

    def clean_data(df):
    df = df.dropna()
    df['bedroom'] = df['bedroom'].astype(int)
    df['fips'] = df['fips'].astype('int')
    df['home_value'] = df['home_value'].astype(int)
    df['square_feet'] = df['square_feet'].astype(int)
    return df