from mycroft import MycroftSkill, intent_file_handler


class SuitenguuEnclosure(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('enclosure.suitenguu.intent')
    def handle_enclosure_suitenguu(self, message):
        self.speak_dialog('enclosure.suitenguu')


def create_skill():
    return SuitenguuEnclosure()

