from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    duration_days: int = Field(ge=1, le=3650)
    budget_millions: float = Field(ge=0.0, le=10000.0)
    mission_status: str = Field(default="planned")

    @model_validator(mode='after')
    def validate(self):
        if self.mission_id[0] != 'M':
            raise ValueError("Mission ID must start with 'M'")
        elif self.crew and len(self.crew) > 0:
            i = 0
            for member in self.crew:
                if (member.rank == Rank.CAPTAIN or
                        member.rank == Rank.COMMANDER):
                    i += 1
            if i == 0:
                raise ValueError(
                    "Mission must have at least one Captain or "
                    "Commander")
        elif self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew
                if member.years_experience >= 5)
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Mission must have at least 50% of crew with "
                    "5+ years of experience")
        elif member.crew:
            for member in self.crew:
                if not member.is_active:
                    raise ValueError(
                        "All crew members must be active for the "
                        "mission")

        return self


def main():
    m = SpaceMission(
        mission_id="MM2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 10, 1),
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=35,
                specialization="Mission Command",
                years_experience=12,
                is_active=True
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=28,
                specialization="Navigation",
                years_experience=6,
                is_active=True
            ),
            CrewMember(
                member_id="C003",
                name="Charlie Lee",
                rank=Rank.OFFICER,
                age=30,
                specialization="engineering",
                years_experience=4,
                is_active=True
            )
        ],
        duration_days=730,
        budget_millions=2500.0
    )
    print(f"""Space Mission Crew Validation
=========================================
Valid mission created:
Mission: {m.mission_name}
ID: {m.mission_id}
Destination: {m.destination}
Duration: {m.duration_days} days
Budget: ${m.budget_millions}M
Crew size: {len(m.crew)}
Crew members:
- {m.crew[0].name} ({m.crew[0].rank}) - {m.crew[0].specialization}
- {m.crew[1].name} ({m.crew[1].rank}) - {m.crew[1].specialization}
- {m.crew[2].name} ({m.crew[2].rank}) - {m.crew[2].specialization}

=================================
""", end="")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="MM2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 10, 1),
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.OFFICER,
                    age=35,
                    specialization="Mission Command",
                    years_experience=12,
                    is_active=True
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=28,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Charlie Lee",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="engineering",
                    years_experience=4,
                    is_active=True
                )
            ],
            duration_days=730,
            budget_millions=2500.0
        )
    except ValidationError as e:
        for err in e.errors():
            print(f"{err['msg']}")


if __name__ == "__main__":
    main()
