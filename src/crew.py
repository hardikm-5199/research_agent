from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import agentstack

@CrewBase
class ResearchagentCrew():
    """research_agent crew"""

    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config['research'],
        )

    @task
    def analyze(self) -> Task:
        return Task(
            config=self.tasks_config['analyze'],
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[*agentstack.tools['perplexity']], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            tools=[], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
        )