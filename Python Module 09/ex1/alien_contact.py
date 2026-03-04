from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("ID must start with AC")
        elif not self.is_verified:
            raise ValueError(
                "Physical contact is not verified")
        elif self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        elif self.signal_strength > 7 and \
                self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")

        return self


def main():
    al = AlienContact(
        contact_id="AC_2024_001",
        is_verified=True,
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli")
    print(f"""Alien Contact Log Validation
======================================
Valid contact report:
ID: {al.contact_id}
Type: {al.contact_type}
Location: {al.location}
Signal: {al.signal_strength}/10
Duration: {al.duration_minutes} minutes
Witnesses: {al.witness_count}
Message: {al.message_received}

======================================
""", end="")
    try:
        print("Expected validation error:")
        AlienContact(
            contact_id="AC_2024_001",
            is_verified=True,
            contact_type=ContactType.PHYSICAL,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=4)
    except ValidationError as e:
        for err in e.errors():
            print(f"{err['msg']}")


if __name__ == "__main__":
    main()
