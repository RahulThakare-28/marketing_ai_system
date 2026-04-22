

class TargetSelector:

    def select(self, df):
        return df[df["probability"] > 0.7]