from typing import Optional, List
from ...modelclass import modelclass


@modelclass
class Underlying:
    "Underlying contains data for an underlying or deliverable associated with an option contract."
    amount: Optional[float] = None
    type: Optional[str] = None
    underlying: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Underlying(**d)


@modelclass
class OptionsContract:
    "OptionsContract contains data for a specified ticker symbol."
    additional_underlyings: Optional[List[Underlying]] = None
    cfi: Optional[str] = None
    correction: Optional[str] = None
    exercise_style: Optional[str] = None
    expiration_date: Optional[str] = None
    primary_exchange: Optional[str] = None
    shares_per_contract: Optional[float] = None
    strike_price: Optional[float] = None
    ticker: Optional[str] = None
    underlying_ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OptionsContract(
            additional_underlyings=None
            if "additional_underlyings" not in d
            else Underlying.from_dict(d["additional_underlyings"]),
            cfi=d.get("cfi", None),
            correction=d.get("correction", None),
            exercise_style=d.get("exercise_style", None),
            expiration_date=d.get("expiration_date", None),
            primary_exchange=d.get("primary_exchange", None),
            shares_per_contract=d.get("shares_per_contract", None),
            strike_price=d.get("strike_price", None),
            size=d.get("size", None),
            ticker=d.get("ticker", None),
            underlying_ticker=d.get("underlying_ticker", None),
        )
