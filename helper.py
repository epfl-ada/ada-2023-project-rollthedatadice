import pandas as pd
import numpy as np
from urllib.parse import urlparse

from wikidataintegrator.wdi_core import WDItemEngine

def convert_freebase_id_to_entity(freebase_id):
    # if freebase_id is NaN，return NaN
    if pd.isnull(freebase_id):
        return np.nan

    # Define query
    sparql_query = f"""
    SELECT
        ?article
    WHERE 
    {{
        ?article schema:about ?item;
        schema:isPartOf <https://en.wikipedia.org/> .
        ?item wdt:P646 "{freebase_id}";
    }}
    """

    # Send the query request to WDQB
    results = WDItemEngine.execute_sparql_query(sparql_query)
    # If you query the result , return the entity name; 
    # otherwise the original freeBase ID will be returned
    if results['results']['bindings']:
        url = results['results']['bindings'][0]['article']['value']

        # Use urlparse to parse URL
        parsed_url = urlparse(url)

        # Extract the name
        article_name = parsed_url.path.split('/')[-1]

        return article_name
    else:
        return freebase_id