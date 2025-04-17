from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CreateCourseCrew():
    """CreateCourseCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def agente_pesquisa_conteudo(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_pesquisa_conteudo'],
            verbose=True,
        )

    @agent
    def agente_planejamento_conteudo(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_planejamento_conteudo'],
            verbose=True,
        )

    @agent
    def agente_redacao_conteudo(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_redacao_conteudo'],
            verbose=True,
        )

    @agent
    def agente_revisao(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_revisao'],
            verbose=True,
        )

    @task
    def pesquisa_conteudo(self) -> Task:
        return Task(
            config=self.tasks_config['pesquisa_conteudo'],
        )

    @task
    def planejamento_conteudo(self) -> Task:
        return Task(
            config=self.tasks_config['planejamento_conteudo'],
        )

    @task
    def redacao_conteudo(self) -> Task:
        return Task(
            config=self.tasks_config['redacao_conteudo'],
        )

    @task
    def revisao_conteudo(self) -> Task:
        return Task(
            config=self.tasks_config['revisao_conteudo'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CreateCourseCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
