from typing import Dict, Iterable, Optional, Sequence, Set, Tuple
import random

"""
This file provides a variety of sample valuation functions for combinatorial auctions,
including additive, substitutes, complements, and mixed valuations. 

You can use these to test convergence and performance of optimisation strategies like LocalBid.
"""

Goods   = Sequence[str]
Bundle  = Iterable[str]
Weights = Dict[str, float]

class AdditionalSampleValuations:
    # Feel free to modify the SINGLE_ITEM_VALS as needed for your experiments
    SINGLE_ITEM_VALS: Weights = {
        'A': 70, 'B': 55, 'C': 85, 'D': 50, 'E': 15, 'F': 65,
        'G': 80, 'H': 90, 'I': 75, 'J': 60, 'K': 40, 'L': 80,
        'M': 90, 'N': 25, 'O': 65, 'P': 70
    }

    @staticmethod
    def additive_valuation(bundle: Bundle) -> float:
        base = AdditionalSampleValuations.SINGLE_ITEM_VALS
        return float(sum(base.get(g, 0.0) for g in bundle))


    # Substitutes 
    @staticmethod
    def substitutes_budget_additive(bundle: Bundle,
                                    B: float = 160.0,
                                    eps_bonus: float = 0.0) -> float:
        """
        Budget-additive: v(S) = min(B, sum_i b_i) + eps_bonus*1{|S|>0}.
        Introduces a budget constraint, capturing some substitutability.
        """
        base = AdditionalSampleValuations.SINGLE_ITEM_VALS
        s = sum(base.get(g, 0.0) for g in bundle)
        return min(B, s) + (eps_bonus if s > 0 else 0.0)

    @staticmethod
    def substitutes_diminishing_weights(bundle: Bundle,
                                        alphas: Sequence[float] = (1.0, 0.8, 0.64, 0.512)) -> float:
        """
        Diminishing weights on the k-th items: v(S) = sum_{i=1..|S|} alpha_i * b_(i),  with b_(i) sorted descending.
        """
        base = AdditionalSampleValuations.SINGLE_ITEM_VALS
        vals = sorted((base.get(g, 0.0) for g in bundle), reverse=True)
        if not vals: return 0.0
        if len(vals) > len(alphas):
            r = alphas[-1] / alphas[-2] if len(alphas) >= 2 else 0.8
            tail = [alphas[-1]*(r**i) for i in range(len(vals) - len(alphas))]
            coeffs = list(alphas) + tail
        else:
            coeffs = list(alphas)
        return sum(a*x for a, x in zip(coeffs, vals))

    # Complements
    @staticmethod
    def complements_pairwise(bundle: Bundle,
                             pair_bonus: Optional[Dict[Tuple[str,str], float]] = None,
                             lambda_pair: float = 0.8) -> float:
        """
        Pairwise synergy: v(S) = sum_i b_i + λ * sum_{(i,j)⊆S} bonus_{ij}, with bonus_{ij} ≥ 0.
        Choose pair_bonus to mark complementary pairs (A,B), (C,D), etc.
        """
        base = AdditionalSampleValuations.SINGLE_ITEM_VALS
        S = list(bundle)
        if not S: return 0.0
        val = sum(base.get(g, 0.0) for g in S)
        # You can modify these default bonuses as needed for your experiments
        if pair_bonus is None:
            pair_bonus = {('A','B'): 60.0, ('C','D'): 50.0}

        bonus_map = {}
        for (i,j), w in pair_bonus.items():
            key = tuple(sorted((i,j)))
            bonus_map[key] = w
        for i in range(len(S)):
            for j in range(i+1, len(S)):
                key = tuple(sorted((S[i], S[j])))
                val += lambda_pair * bonus_map.get(key, 0.0)
        return val

    # mixed valuation: substitutes + complements
    @staticmethod
    def mixed_valuation(bundle: Bundle,
                              budget_B: float = 160.0,
                              pair_bonus: Optional[Dict[Tuple[str,str], float]] = None,
                              lambda_pair: float = 0.6) -> float:
        """
        Blend a substitutes component (budget-additive) with localized pairwise complements:
        """
        sub_part = AdditionalSampleValuations.substitutes_budget_additive(bundle, B=budget_B)
        comp_part = AdditionalSampleValuations.complements_pairwise(bundle, pair_bonus, lambda_pair) \
                    - AdditionalSampleValuations.additive_valuation(bundle)
        return sub_part + comp_part


    # Random price generators
    @staticmethod
    def generate_price_vector(spread: float = 25.0, clip: Tuple[float,float] = (0.0, 200.0)) -> Dict[str,float]:
        """
        Independent prices around base values (uniform window).
        """
        low, high = clip
        out = {}
        for item, base in AdditionalSampleValuations.SINGLE_ITEM_VALS.items():
            p = random.uniform(base - spread, base + spread)
            out[item] = min(high, max(low, p))
        return out

    