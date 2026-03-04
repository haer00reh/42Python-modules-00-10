from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    s = SpaceStation(
        station_id="ISS001",
        crew_size="5",
        name="International Space Station",
        oxygen_level="85.5",
        power_level="92.3",
    )
    print(f"""Space Station Data Validation
========================================
Valid station created:
ID: {s.station_id}
Name: {s.name}
Crew: {s.crew_size} People
Power: {s.power_level}%
Oxygen: {s.oxygen_level}%
Status: {'Operational' if s.is_operational else 'is not Operational'}

========================================
""")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS001",
            crew_size="200",
            name="International Space Station",
            oxygen_level="285.5",
            power_level="92.3",
        )
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
