import aiohttp
from rich.console import Console
from typing import Optional
from src.models.ip_info import IpInfo

console = Console()


class IpInfoService:
    BASE_URL = "https://ipinfo.io/"

    async def get_ip_info(self, ip: str) -> Optional[IpInfo]:
        url = f"{self.BASE_URL}{ip}/json"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        console.print(f"[red]Erro HTTP {response.status} ao consultar {url}[/red]")
                        return None

                    data = await response.json()
                    console.print("[green][+][/green] Requisição concluída com sucesso")
                    return IpInfo(**data)

            except aiohttp.ClientError as e:
                console.print(f"[red][HTTP ERROR][/red] {str(e)}")
            except Exception as ex:
                console.print(f"[red][ERROR][/red] {str(ex)}")

        return None
