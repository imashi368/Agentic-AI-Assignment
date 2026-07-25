class VerifierAgent:
    def verify(self, answer):
        if not answer or len(answer.strip()) < 2:
            return "Unable to find enough information."
        return answer