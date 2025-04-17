#!/usr/bin/env python
import sys
import warnings
from crewai import agent
from dotenv import load_dotenv, find_dotenv
import agentops
import os
from datetime import datetime
import openai
from crew import CrewOfCrewProject

load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')
agentops_api_key = os.getenv('AGENTOPS_API_KEY')
agentops.init(api_key=agentops_api_key, default_tags=['crewai-simple'])

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

SISTEMA = '''Um sistema para criação de uma crew que desenvolve
conteudo para cursos em python. Primeiro faz uma pesquisa de conteúdos 
relevantes, levanta tópicos importante dentro desse conteúdo, desenvolve
um escopo, redige a apostila do curso e revisa'''

def run():
    """
    Run the crew.
    """
    inputs = {
        'definicao_do_sistema': SISTEMA,
        'current_year': str(datetime.now().year)
    }
    
    try:
        CrewOfCrewProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CrewOfCrewProject().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewOfCrewProject().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        CrewOfCrewProject().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
