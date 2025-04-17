from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CrewOfCrewProject():
    """CrewOfCrewProject crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def arquiteto_de_sistemas(self) -> Agent:
        return Agent(
            config=self.agents_config['arquiteto_de_sistemas'],
            verbose=True
        )

    @agent
    def engenheiro_de_ia(self) -> Agent:
        return Agent(
            config=self.agents_config['engenheiro_de_ia'],
            verbose=True
        )

    @agent
    def desenvolvedor_backend(self) -> Agent:
        return Agent(
            config=self.agents_config['desenvolvedor_backend'],
            verbose=True
        )

    @agent
    def engenheiro_de_qa(self) -> Agent:
        return Agent(
            config=self.agents_config['engenheiro_de_qa'],
            verbose=True
        )

    @task
    def especificar_requisitos_sistema_multi_agents(self) -> Task:
        return Task(
            config=self.tasks_config['especificar_requisitos_sistema_multi_agents'],
        )

    @task
    def modelar_arquitetura_multi_agents(self) -> Task:
        return Task(
            config=self.tasks_config['modelar_arquitetura_multi_agents'],
        )

    @task
    def definir_documentar_agentes(self) -> Task:
        return Task(
            config=self.tasks_config['definir_documentar_agentes'],
        )

    @task
    def elaborar_tasks_e_workflows(self) -> Task:
        return Task(
            config=self.tasks_config['elaborar_tasks_e_workflows'],
        )

    @task
    def implementar_crew_py_e_integracoes(self) -> Task:
        return Task(
            config=self.tasks_config['implementar_crew_py_e_integracoes'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewOfCrewProject crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
