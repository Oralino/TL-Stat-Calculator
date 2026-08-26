import tkinter as tk
from tkinter import ttk, messagebox

# Color configuration for dark theme
BG_DARK = "#1e1e1e"
BG_PANEL = "#2d2d2d"
BG_ENTRY = "#3c3c3c"
ACCENT_BLUE = "#007acc"
TEXT_LIGHT = "#e0e0e0"

# Font definitions
FONT_FAMILY = "Google Sans"
FONT_NORMAL = (FONT_FAMILY, 10)
FONT_BOLD = (FONT_FAMILY, 11, "bold")
FONT_BUTTON = (FONT_FAMILY, 10, "bold")

def calculate_evasion():
    try:
        evasion = float(entry_evasion.get())
        hit = float(entry_hit.get())
        
        diff = evasion - hit
        chance = (diff / (diff + 1000)) * 100 if diff > 0 else 0.0
            
        label_evasion_result.config(text=f"Evasion Chance: {chance:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Evasion and Hit.")

def calculate_crit():
    try:
        crit = float(entry_crit.get())
        endurance = float(entry_endurance.get())
        
        diff = crit - endurance
        chance = (diff / (diff + 1000)) * 100 if diff > 0 else 0.0
            
        label_crit_result.config(text=f"Crit Chance: {chance:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Crit and Endurance.")

def calculate_heavy():
    try:
        heavy = float(entry_heavy.get())
        heavy_eva = float(entry_heavy_eva.get())
        
        diff = heavy - heavy_eva
        chance = (diff / (diff + 1000)) * 100 if diff > 0 else 0.0
            
        label_heavy_result.config(text=f"Double Damage Chance: {chance:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Heavy Attack and Heavy Evasion.")

def calculate_skill_damage():
    try:
        sdb = float(entry_sdb.get())
        sdr = float(entry_sdr.get())
        
        if sdb > sdr:
            net_sdb = sdb - sdr
            net_pct = (net_sdb / (net_sdb + 1000)) * 100
            result_text = (
                f"Net Difference: {net_sdb:.0f} SDB over SDR\n\n"
                f"Effective Skill Damage Boost: {net_pct:.2f}%"
            )
        elif sdr > sdb:
            net_sdr = sdr - sdb
            net_pct = (net_sdr / (net_sdr + 1000)) * 100
            result_text = (
                f"Net Difference: {net_sdr:.0f} SDR over SDB\n\n"
                f"Effective Skill Damage Resistance: {net_pct:.2f}%"
            )
        else:
            result_text = "Net Difference: 0 (Equal Stats)\n\nNet Modifier: 0.00%"
            
        label_sdb_result.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for SDB and SDR.")

def calculate_defense_comparison():
    try:
        curr_def = float(entry_curr_def.get())
        damage_taken = float(entry_damage_taken.get())
        target_def = float(entry_target_def.get())
        
        if curr_def < 0 or target_def < 0 or damage_taken < 0:
            messagebox.showerror("Input Error", "Values must be non-negative.")
            return

        curr_mitigation = curr_def / (curr_def + 2500)
        
        if curr_mitigation < 1.0:
            raw_damage = damage_taken / (1.0 - curr_mitigation)
        else:
            raw_damage = damage_taken

        target_mitigation = target_def / (target_def + 2500)
        new_damage = raw_damage * (1.0 - target_mitigation)

        result_text = (
            f"Current Mitigation: {curr_mitigation * 100:.2f}%\n"
            f"Target Mitigation: {target_mitigation * 100:.2f}%\n\n"
            f"New Damage Taken: {new_damage:.1f}"
        )
        label_defense_result.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Defense and Damage Taken.")

def calculate_chance_res():
    try:
        chance_stat = float(entry_chance.get())
        res_stat = float(entry_res.get())
        
        diff = chance_stat - res_stat
        if diff >= 0:
            mod = (diff / (diff + 250)) * 100
            label_chance_result.config(text=f"Bonus Chance Modifier: +{mod:.2f}%")
        else:
            abs_diff = abs(diff)
            mod = (abs_diff / (abs_diff + 250)) * 100
            label_chance_result.config(text=f"Chance Penalty Modifier: -{mod:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Status Chance and Resistance.")

def calculate_cc_hit():
    try:
        user_cc_chance = float(entry_cc_chance.get())
        target_resistance = float(entry_cc_res.get())
        z = float(entry_cc_base.get())
        
        w = 100.0 - z
        
        if target_resistance > user_cc_chance:
            x = target_resistance - user_cc_chance
            land_chance = z * (1.0 - (x / (250.0 + x)))
        elif user_cc_chance > target_resistance:
            x = user_cc_chance - target_resistance
            land_chance = z + (w * (x / (250.0 + x)))
        else:
            land_chance = z

        land_chance = max(0.0, min(100.0, land_chance))
        miss_chance = 100.0 - land_chance
        
        label_cc_result.config(text=f"Final CC Land Chance: {land_chance:.1f}%\nFinal CC Miss Chance: {miss_chance:.1f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for CC Chance, Resistance, and Base Hit Chance.")

def calculate_crit_damage():
    try:
        max_base = float(entry_crit_base.get())
        boost = float(entry_crit_boost.get())
        resist = float(entry_crit_resist.get())
        
        eff_boost = max(0.0, boost - resist)
        final_damage = max_base * (1.0 + (eff_boost / 100.0))
        
        result_text = (
            f"Effective Boost: {eff_boost:.2f}%\n"
            f"Final Crit Damage: {final_damage:.1f}"
        )
        label_crit_dmg_result.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Base Damage, Boost, and Resistance.")

def calculate_heavy_damage():
    try:
        base_dmg = float(entry_heavy_base.get())
        boost = float(entry_heavy_boost.get())
        resist = float(entry_heavy_resist.get())
        
        net = (boost - resist) / 100.0
        multiplier = max(1.5, 2.0 + net)
        final_damage = base_dmg * multiplier
        
        result_text = (
            f"Damage Multiplier: {multiplier:.2f}x\n"
            f"Final Heavy Damage: {final_damage:.1f}"
        )
        label_heavy_dmg_result.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Base Damage, Boost, and Resistance.")

def calculate_def_vs_crit():
    try:
        def_a = float(entry_dvc_def_a.get())
        def_b = float(entry_dvc_def_b.get())
        dmg_taken = float(entry_dvc_dmg.get())
        
        crit_res_a = float(entry_dvc_crit_res_a.get())
        crit_res_b = float(entry_dvc_crit_res_b.get())
        enemy_crit_boost = float(entry_dvc_enemy_crit_boost.get())

        # Baseline assumption: Incoming hit is based on Option A's stats
        mit_a = def_a / (def_a + 2500)
        eff_boost_a = max(0.0, enemy_crit_boost - crit_res_a)
        
        # Calculate raw unmitigated base hit from the incoming crit hit
        raw_hit = dmg_taken / (1.0 + (eff_boost_a / 100.0)) if dmg_taken > 0 else 0
        raw_base_hit = raw_hit / (1.0 - mit_a) if mit_a < 1.0 else raw_hit

        # Option A Final Hit Calculation
        final_crit_a = dmg_taken

        # Option B Final Hit Calculation
        mit_b = def_b / (def_b + 2500)
        base_dmg_b = raw_base_hit * (1.0 - mit_b)
        eff_boost_b = max(0.0, enemy_crit_boost - crit_res_b)
        final_crit_b = base_dmg_b * (1.0 + (eff_boost_b / 100.0))

        saved_a = 0.0
        saved_b = dmg_taken - final_crit_b

        res_text = (
            f"Option A ({def_a:.0f} Def / {crit_res_a:.2f}% Res): {final_crit_a:.1f} hit taken\n"
            f"Option B ({def_b:.0f} Def / {crit_res_b:.2f}% Res): {final_crit_b:.1f} hit taken\n\n"
        )

        if final_crit_a < final_crit_b:
            res_text += f"Verdict: Option A is better (Saves {final_crit_b - final_crit_a:.1f} more HP)."
        elif final_crit_b < final_crit_a:
            res_text += f"Verdict: Option B is better (Saves {final_crit_a - final_crit_b:.1f} more HP)."
        else:
            res_text += "Verdict: Both options result in equal damage taken."

        label_dvc_result.config(text=res_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all comparison fields.")

def create_tab_content(tab):
    tab.columnconfigure(0, weight=1)
    content_frame = ttk.Frame(tab)
    content_frame.grid(row=0, column=0, pady=20)
    return content_frame

# Initialize window
root = tk.Tk()
root.title("Throne & Liberty Hidden Stat Calculator")
root.geometry("540x660")
root.resizable(True, True)
root.configure(bg=BG_DARK)

# Custom styles
style = ttk.Style()
style.theme_use("default")

style.configure("TFrame", background=BG_PANEL)
style.configure("TNotebook", background=BG_DARK, borderwidth=0)
style.configure("TNotebook.Tab", background=BG_PANEL, foreground=TEXT_LIGHT, padding=[5, 5], font=FONT_NORMAL)
style.map("TNotebook.Tab", background=[("selected", ACCENT_BLUE)], foreground=[("selected", "#ffffff")])

style.configure("TLabel", background=BG_PANEL, foreground=TEXT_LIGHT, font=FONT_NORMAL)
style.configure("Result.TLabel", background=BG_PANEL, foreground="#4ec9b0", font=FONT_BOLD, anchor="center", justify="center")

style.configure("TEntry", fieldbackground=BG_ENTRY, foreground=TEXT_LIGHT, insertcolor=TEXT_LIGHT, font=FONT_NORMAL, justify="center")
style.configure("TButton", background=ACCENT_BLUE, foreground="#ffffff", font=FONT_BUTTON, borderwidth=0)
style.map("TButton", background=[("active", "#005999")])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Tab 1: Hit & Evasion
tab_evasion = ttk.Frame(notebook)
notebook.add(tab_evasion, text="Evasion")
frame_evasion = create_tab_content(tab_evasion)

ttk.Label(frame_evasion, text="Your Evasion:").grid(row=0, column=0, padx=(0, 10), pady=15, sticky="e")
entry_evasion = ttk.Entry(frame_evasion)
entry_evasion.grid(row=0, column=1, pady=15, sticky="w")

ttk.Label(frame_evasion, text="Enemy Hit:").grid(row=1, column=0, padx=(0, 10), pady=15, sticky="e")
entry_hit = ttk.Entry(frame_evasion)
entry_hit.grid(row=1, column=1, pady=15, sticky="w")

btn_evasion = ttk.Button(frame_evasion, text="Calculate", command=calculate_evasion)
btn_evasion.grid(row=2, column=0, columnspan=2, pady=15)

label_evasion_result = ttk.Label(frame_evasion, text="Evasion Chance: 0.00%", style="Result.TLabel")
label_evasion_result.grid(row=3, column=0, columnspan=2, pady=15)

# Tab 2: Crit Rate
tab_crit = ttk.Frame(notebook)
notebook.add(tab_crit, text="Crit Rate")
frame_crit = create_tab_content(tab_crit)

ttk.Label(frame_crit, text="Your Critical Hit:").grid(row=0, column=0, padx=(0, 10), pady=15, sticky="e")
entry_crit = ttk.Entry(frame_crit)
entry_crit.grid(row=0, column=1, pady=15, sticky="w")

ttk.Label(frame_crit, text="Enemy Endurance:").grid(row=1, column=0, padx=(0, 10), pady=15, sticky="e")
entry_endurance = ttk.Entry(frame_crit)
entry_endurance.grid(row=1, column=1, pady=15, sticky="w")

btn_crit = ttk.Button(frame_crit, text="Calculate", command=calculate_crit)
btn_crit.grid(row=2, column=0, columnspan=2, pady=15)

label_crit_result = ttk.Label(frame_crit, text="Crit Chance: 0.00%", style="Result.TLabel")
label_crit_result.grid(row=3, column=0, columnspan=2, pady=15)

# Tab 3: Crit Dmg
tab_crit_dmg = ttk.Frame(notebook)
notebook.add(tab_crit_dmg, text="Crit Dmg")
frame_crit_dmg = create_tab_content(tab_crit_dmg)

ttk.Label(frame_crit_dmg, text="Max Base Damage:").grid(row=0, column=0, padx=(0, 10), pady=10, sticky="e")
entry_crit_base = ttk.Entry(frame_crit_dmg)
entry_crit_base.grid(row=0, column=1, pady=10, sticky="w")

ttk.Label(frame_crit_dmg, text="Crit Damage Boost (%):").grid(row=1, column=0, padx=(0, 10), pady=10, sticky="e")
entry_crit_boost = ttk.Entry(frame_crit_dmg)
entry_crit_boost.insert(0, "0")
entry_crit_boost.grid(row=1, column=1, pady=10, sticky="w")

ttk.Label(frame_crit_dmg, text="Enemy Crit Resistance (%):").grid(row=2, column=0, padx=(0, 10), pady=10, sticky="e")
entry_crit_resist = ttk.Entry(frame_crit_dmg)
entry_crit_resist.insert(0, "0")
entry_crit_resist.grid(row=2, column=1, pady=10, sticky="w")

btn_crit_dmg = ttk.Button(frame_crit_dmg, text="Calculate", command=calculate_crit_damage)
btn_crit_dmg.grid(row=3, column=0, columnspan=2, pady=12)

label_crit_dmg_result = ttk.Label(frame_crit_dmg, text="Effective Boost: 0.00%\nFinal Crit Damage: 0.0", style="Result.TLabel")
label_crit_dmg_result.grid(row=4, column=0, columnspan=2, pady=10)

# Tab 4: Heavy Rate
tab_heavy = ttk.Frame(notebook)
notebook.add(tab_heavy, text="Heavy Rate")
frame_heavy = create_tab_content(tab_heavy)

ttk.Label(frame_heavy, text="Your Heavy Attack:").grid(row=0, column=0, padx=(0, 10), pady=15, sticky="e")
entry_heavy = ttk.Entry(frame_heavy)
entry_heavy.grid(row=0, column=1, pady=15, sticky="w")

ttk.Label(frame_heavy, text="Enemy Heavy Evasion:").grid(row=1, column=0, padx=(0, 10), pady=15, sticky="e")
entry_heavy_eva = ttk.Entry(frame_heavy)
entry_heavy_eva.insert(0, "0")
entry_heavy_eva.grid(row=1, column=1, pady=15, sticky="w")

btn_heavy = ttk.Button(frame_heavy, text="Calculate", command=calculate_heavy)
btn_heavy.grid(row=2, column=0, columnspan=2, pady=15)

label_heavy_result = ttk.Label(frame_heavy, text="Double Damage Chance: 0.00%", style="Result.TLabel")
label_heavy_result.grid(row=3, column=0, columnspan=2, pady=15)

# Tab 5: Heavy Dmg
tab_heavy_dmg = ttk.Frame(notebook)
notebook.add(tab_heavy_dmg, text="Heavy Dmg")
frame_heavy_dmg = create_tab_content(tab_heavy_dmg)

ttk.Label(frame_heavy_dmg, text="Base Damage:").grid(row=0, column=0, padx=(0, 10), pady=10, sticky="e")
entry_heavy_base = ttk.Entry(frame_heavy_dmg)
entry_heavy_base.grid(row=0, column=1, pady=10, sticky="w")

ttk.Label(frame_heavy_dmg, text="Heavy Damage Boost (%):").grid(row=1, column=0, padx=(0, 10), pady=10, sticky="e")
entry_heavy_boost = ttk.Entry(frame_heavy_dmg)
entry_heavy_boost.insert(0, "0")
entry_heavy_boost.grid(row=1, column=1, pady=10, sticky="w")

ttk.Label(frame_heavy_dmg, text="Enemy Heavy Resistance (%):").grid(row=2, column=0, padx=(0, 10), pady=10, sticky="e")
entry_heavy_resist = ttk.Entry(frame_heavy_dmg)
entry_heavy_resist.insert(0, "0")
entry_heavy_resist.grid(row=2, column=1, pady=10, sticky="w")

btn_heavy_dmg = ttk.Button(frame_heavy_dmg, text="Calculate", command=calculate_heavy_damage)
btn_heavy_dmg.grid(row=3, column=0, columnspan=2, pady=12)

label_heavy_dmg_result = ttk.Label(frame_heavy_dmg, text="Damage Multiplier: 2.00x\nFinal Heavy Damage: 0.0", style="Result.TLabel")
label_heavy_dmg_result.grid(row=4, column=0, columnspan=2, pady=10)

# Tab 6: Skill Damage Comparison
tab_skill = ttk.Frame(notebook)
notebook.add(tab_skill, text="Skill Dmg")
frame_skill = create_tab_content(tab_skill)

ttk.Label(frame_skill, text="Skill Damage Boost (SDB):").grid(row=0, column=0, padx=(0, 10), pady=15, sticky="e")
entry_sdb = ttk.Entry(frame_skill)
entry_sdb.grid(row=0, column=1, pady=15, sticky="w")

ttk.Label(frame_skill, text="Skill Damage Resistance (SDR):").grid(row=1, column=0, padx=(0, 10), pady=15, sticky="e")
entry_sdr = ttk.Entry(frame_skill)
entry_sdr.grid(row=1, column=1, pady=15, sticky="w")

btn_skill = ttk.Button(frame_skill, text="Calculate", command=calculate_skill_damage)
btn_skill.grid(row=2, column=0, columnspan=2, pady=15)

label_sdb_result = ttk.Label(frame_skill, text="Net Difference: 0\n\nNet Modifier: 0.00%", style="Result.TLabel")
label_sdb_result.grid(row=3, column=0, columnspan=2, pady=15)

# Tab 7: Defense
tab_defense = ttk.Frame(notebook)
notebook.add(tab_defense, text="Defense")
frame_defense = create_tab_content(tab_defense)

ttk.Label(frame_defense, text="Current Defense:").grid(row=0, column=0, padx=(0, 10), pady=10, sticky="e")
entry_curr_def = ttk.Entry(frame_defense)
entry_curr_def.grid(row=0, column=1, pady=10, sticky="w")

ttk.Label(frame_defense, text="Damage Received:").grid(row=1, column=0, padx=(0, 10), pady=10, sticky="e")
entry_damage_taken = ttk.Entry(frame_defense)
entry_damage_taken.grid(row=1, column=1, pady=10, sticky="w")

ttk.Label(frame_defense, text="Target Defense:").grid(row=2, column=0, padx=(0, 10), pady=10, sticky="e")
entry_target_def = ttk.Entry(frame_defense)
entry_target_def.grid(row=2, column=1, pady=10, sticky="w")

btn_defense = ttk.Button(frame_defense, text="Calculate", command=calculate_defense_comparison)
btn_defense.grid(row=3, column=0, columnspan=2, pady=12)

label_defense_result = ttk.Label(frame_defense, text="Current Mitigation: 0.00%\nTarget Mitigation: 0.00%\n\nNew Damage Taken: 0.0", style="Result.TLabel")
label_defense_result.grid(row=4, column=0, columnspan=2, pady=10)

# Tab 8: Def vs Crit Res (Updated UI and corrected Option Labels)
tab_def_vs_crit = ttk.Frame(notebook)
notebook.add(tab_def_vs_crit, text="Def vs Crit Res")
frame_dvc = create_tab_content(tab_def_vs_crit)

ttk.Label(frame_dvc, text="Defense A:").grid(row=0, column=0, padx=(0, 10), pady=6, sticky="e")
entry_dvc_def_a = ttk.Entry(frame_dvc)
entry_dvc_def_a.grid(row=0, column=1, pady=6, sticky="w")

ttk.Label(frame_dvc, text="Defense B:").grid(row=1, column=0, padx=(0, 10), pady=6, sticky="e")
entry_dvc_def_b = ttk.Entry(frame_dvc)
entry_dvc_def_b.grid(row=1, column=1, pady=6, sticky="w")

ttk.Label(frame_dvc, text="Incoming Crit Hit Recv:").grid(row=2, column=0, padx=(0, 10), pady=6, sticky="e")
entry_dvc_dmg = ttk.Entry(frame_dvc)
entry_dvc_dmg.grid(row=2, column=1, pady=6, sticky="w")

ttk.Label(frame_dvc, text="Crit Res A (%):").grid(row=3, column=0, padx=(0, 10), pady=6, sticky="e")
entry_dvc_crit_res_a = ttk.Entry(frame_dvc)
entry_dvc_crit_res_a.insert(0, "0")
entry_dvc_crit_res_a.grid(row=3, column=1, pady=6, sticky="w")

ttk.Label(frame_dvc, text="Crit Res B (%):").grid(row=4, column=0, padx=(0, 10), pady=6, sticky="e")
entry_dvc_crit_res_b = ttk.Entry(frame_dvc)
entry_dvc_crit_res_b.insert(0, "0")
entry_dvc_crit_res_b.grid(row=4, column=1, pady=6, sticky="w")

ttk.Label(frame_dvc, text="Enemy Crit Boost (%):").grid(row=5, column=0, padx=(0, 10), pady=6, sticky="e")
entry_dvc_enemy_crit_boost = ttk.Entry(frame_dvc)
entry_dvc_enemy_crit_boost.insert(0, "40")
entry_dvc_enemy_crit_boost.grid(row=5, column=1, pady=6, sticky="w")

btn_dvc = ttk.Button(frame_dvc, text="Compare Trade-off", command=calculate_def_vs_crit)
btn_dvc.grid(row=6, column=0, columnspan=2, pady=12)

label_dvc_result = ttk.Label(frame_dvc, text="Option A: 0.0\nOption B: 0.0\n\nVerdict: N/A", style="Result.TLabel")
label_dvc_result.grid(row=7, column=0, columnspan=2, pady=8)

# Tab 9: Status Res
tab_chance = ttk.Frame(notebook)
notebook.add(tab_chance, text="Status Res")
frame_chance = create_tab_content(tab_chance)

ttk.Label(frame_chance, text="Your Status Chance:").grid(row=0, column=0, padx=(0, 10), pady=15, sticky="e")
entry_chance = ttk.Entry(frame_chance)
entry_chance.grid(row=0, column=1, pady=15, sticky="w")

ttk.Label(frame_chance, text="Enemy Resistance:").grid(row=1, column=0, padx=(0, 10), pady=15, sticky="e")
entry_res = ttk.Entry(frame_chance)
entry_res.grid(row=1, column=1, pady=15, sticky="w")

btn_chance = ttk.Button(frame_chance, text="Calculate", command=calculate_chance_res)
btn_chance.grid(row=2, column=0, columnspan=2, pady=15)

label_chance_result = ttk.Label(frame_chance, text="Chance Modifier: 0.00%", style="Result.TLabel")
label_chance_result.grid(row=3, column=0, columnspan=2, pady=15)

# Tab 10: CC Hit
tab_cc = ttk.Frame(notebook)
notebook.add(tab_cc, text="CC Hit")
frame_cc = create_tab_content(tab_cc)

ttk.Label(frame_cc, text="Your CC Chance:").grid(row=0, column=0, padx=(0, 10), pady=12, sticky="e")
entry_cc_chance = ttk.Entry(frame_cc)
entry_cc_chance.grid(row=0, column=1, pady=12, sticky="w")

ttk.Label(frame_cc, text="Target CC Resistance:").grid(row=1, column=0, padx=(0, 10), pady=12, sticky="e")
entry_cc_res = ttk.Entry(frame_cc)
entry_cc_res.grid(row=1, column=1, pady=12, sticky="w")

ttk.Label(frame_cc, text="Skill Base Hit Chance (%):").grid(row=2, column=0, padx=(0, 10), pady=12, sticky="e")
entry_cc_base = ttk.Entry(frame_cc)
entry_cc_base.insert(0, "80")
entry_cc_base.grid(row=2, column=1, pady=12, sticky="w")

btn_cc = ttk.Button(frame_cc, text="Calculate", command=calculate_cc_hit)
btn_cc.grid(row=3, column=0, columnspan=2, pady=15)

label_cc_result = ttk.Label(frame_cc, text="Final CC Land Chance: 0.0%\nFinal CC Miss Chance: 0.0%", style="Result.TLabel")
label_cc_result.grid(row=4, column=0, columnspan=2, pady=12)

root.mainloop()