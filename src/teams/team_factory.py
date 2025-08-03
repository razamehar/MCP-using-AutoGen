from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination


def create_team(agents):

    team = RoundRobinGroupChat(
        participants=agents,
        max_turns=2,
        termination_condition=TextMentionTermination('TERMINATE')
    )

    return team