

class TargetSelector:

    def select(self, df):
        # -----------------------------
        # ✅ STEP 1: Remove duplicates (IMPORTANT)
        # -----------------------------
        df = df.groupby("user_id", as_index=False).agg({
            "probability": "mean"   # OR "max"
        })

        # -----------------------------
        # ✅ STEP 2: Apply threshold
        # -----------------------------
        df = df[df["probability"] > 0.3]

        return df