# Data Extraction [Inference Module]
# Currently supports a few instances of quandl imports
# Attempts to infer call to closest match (Edit Distance)
import yahoo_finance as yahoo
import quandl
import distance

# List of functions to extract data
func = {
    "quandl": lambda x: quandl.get(x[0]),
    "yahoo": lambda x: yahoo.Share(x[0]).get_historical('2016-05-05', '2016-06-06')
}

# Collection of extraction methods and arguments
Collection = {
    # Each key (of type String) maps to a vector
    # corresponding to [(function), [argument list]]
    "US Rates": [func["quandl"], ["FED/SVENY"]],
    "USD/SGD FX": [func["quandl"], ["FED/RXI_N_A_SI"]],
    "Google": [func["yahoo"], ["GOOGL"]]
}


# TODO: Add regex interpreter
def extract(inquiry):
    arg = correction(inquiry)
    return Collection[arg][0](Collection[arg][1])


def correction(inquiry):
    m = 9999.0
    sol = ""
    for key in Collection.keys():
        d = distance.nlevenshtein(inquiry, key)
        if d < m:
            m = d
            sol = key
    return sol
