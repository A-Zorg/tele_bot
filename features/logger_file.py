import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:/Users/sasa/PycharmProjects/FinBot/Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger