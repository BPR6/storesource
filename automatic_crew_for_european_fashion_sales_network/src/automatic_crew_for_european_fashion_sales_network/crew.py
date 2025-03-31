from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SeleniumScrapingTool

@CrewBase
class AutomaticCrewForEuropeanFashionSalesNetworkCrew():
    """AutomaticCrewForEuropeanFashionSalesNetwork crew"""

    @agent
    def data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['data_collector'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def shop_crawler(self) -> Agent:
        return Agent(
            config=self.agents_config['shop_crawler'],
            tools=[WebsiteSearchTool(), ScrapeWebsiteTool(), SeleniumScrapingTool()],
        )

    @agent
    def data_filter(self) -> Agent:
        return Agent(
            config=self.agents_config['data_filter'],
            tools=[],
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            tools=[],
        )


    @task
    def gather_cities_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_cities_task'],
            tools=[WebsiteSearchTool()],
        )

    @task
    def crawl_shops_task(self) -> Task:
        return Task(
            config=self.tasks_config['crawl_shops_task'],
            tools=[WebsiteSearchTool(), ScrapeWebsiteTool(), SeleniumScrapingTool()],
        )

    @task
    def filter_shops_task(self) -> Task:
        return Task(
            config=self.tasks_config['filter_shops_task'],
            tools=[],
        )

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_report_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AutomaticCrewForEuropeanFashionSalesNetwork crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
