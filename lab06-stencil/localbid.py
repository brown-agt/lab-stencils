from marginal_value import calculate_marginal_value
from sample_valuations import SampleValuations
#from sample_valuations_experiments import AdditionalSampleValuations

def local_bid(goods, valuation_function, price_vector, num_iterations=100):
    """
    Use local bid to iteratively set the bid vectors to our marginal values 

    TODO: Fill in local bid as described in the pseudocode in the assignment.
    """

    raise NotImplementedError

if __name__ == "__main__":
    goods = set(SampleValuations.SINGLE_ITEM_VALS.keys())
    price_vector = SampleValuations.generate_price_vector() 

    for valuation_func in [
        SampleValuations.additive_valuation,
        SampleValuations.complement_valuation,
        SampleValuations.substitute_valuation,
        SampleValuations.randomized_valuation
    ]:
        print(f"Running LocalBid with {valuation_func.__name__}:")
        optimized_bids = local_bid(goods, valuation_func, price_vector, num_iterations=100)
        print("Final bid vector:", optimized_bids, "\n")
    
    """
    # Test with more complex valuations after implementing local bid.
    # You will have to force convergence by implementing exponential smoothing in Local Bid.

    Use - from sample_valuations_experiments import SampleValuations; and 
    comment out - from sample_valuations import SampleValuations at the top.
    Use the code below to run these extra experiments.
    """
    
    """
    goods = set(AdditionalSampleValuations.SINGLE_ITEM_VALS.keys())
    price_vector = AdditionalSampleValuations.generate_price_vector_independent() 
    print("Initial price vector:", dict(sorted(price_vector.items())), "\n")
    for valuation_func in [
        AdditionalSampleValuations.additive_valuation,
        AdditionalSampleValuations.complements_pairwise,
        AdditionalSampleValuations.substitutes_diminishing_weights,
        AdditionalSampleValuations.mixed_valuation
    ]:
        print(f"Running LocalBid with {valuation_func.__name__}:")
        optimized_bids = local_bid(goods, valuation_func, price_vector, num_iterations=100)
        print("Final bid vector:", optimized_bids, "\n")
    """