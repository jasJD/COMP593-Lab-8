from cgitb import text
from tkinter import *
from tkinter import ttk
from pokemonInfoView import get_poke_info


def main():
    
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap("Poke-Ball1.ico")
    root.geometry('400x400')




    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2, padx=25, pady=25)
 
    frm_info = ttk.LabelFrame(root, text="Infomation")
    frm_info.grid(row=1, column=0, padx=25, pady=25, sticky=N)
 
    frm_stats = ttk.LabelFrame(root, text="Status")
    frm_stats.grid(row=1, column=1, padx=20, pady=20, sticky=N)
    
    lbl_name = ttk.Label(frm_user_input, text="Pokemon Name =")
    lbl_name.grid(row=0, column=0, padx=10, pady=10)
    
    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=0, column=1, pady=10)

    def btn_getinfo_click():
        pokemon_name = ent_name.get()
        poke_dict = get_poke_info(pokemon_name)
        
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + 'dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + 'dm'
            types_list = (t['type']['name'] for t in poke_dict['types'])
            lbl_type_val['text']=', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defense['value'] = poke_dict['stats'][2]['base_stat']
            prg_special_attack['value'] = poke_dict['stats'][3]['base_stat']
            prg_special_defense['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']

            
    btwn_get_info = ttk.Button(frm_user_input, text = "GET INFO", command=btn_getinfo_click)
    btwn_get_info.grid(row=0, column=2, padx=10, pady=10)
    
    lbl_height = ttk.Label(frm_info, text='Height:')
    lbl_height.grid(row=100, column=100, padx=(10,0), pady=10, sticky=E)
    lbl_height_val = ttk.Label(frm_info, text='TBD')
    lbl_height_val.grid(row=100, column=200, padx=20, pady=10)
    
    lbl_weight = ttk.Label(frm_info, text='Weight:')
    lbl_weight.grid(row=300, column=100, padx=(10,0), pady=10, sticky=E)
    lbl_weight_val = ttk.Label(frm_info, text='TBD')
    lbl_weight_val.grid(row=300, column=200, padx=20, pady=10)
    
    lbl_type = ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=500, column=100, padx=(10,0), pady=10, sticky=E)
    lbl_type_val = ttk.Label(frm_info, text='TBD')
    lbl_type_val.grid(row=500, column=200, padx=20, pady=10)
    
    lbl_hp = ttk.Label(frm_stats, text='HP:')
    lbl_hp.grid(row=100, column=100, padx=(10,0), pady=10, sticky=E)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_hp.grid(row=100, column=200, padx=(5,10), pady=10, sticky=W)
    
    lbl_attack = ttk.Label(frm_stats, text='Attack:')
    lbl_attack.grid(row=200, column=100, padx=(10,0), pady=10, sticky=E)
    prg_attack = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_attack.grid(row=200, column=200, padx=(5,10), sticky=W)
    
    lbl_defense = ttk.Label(frm_stats, text='Defense:')
    lbl_defense.grid(row=300, column=100, padx=(10,0), pady=10, sticky=E)
    prg_defense = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_defense.grid(row=300, column=200, padx=(5,10), sticky=W)
    
    lbl_special_attack = ttk.Label(frm_stats, text='Special Attack:')
    lbl_special_attack.grid(row=400, column=100, padx=(10,0), pady=10, sticky=E)
    prg_special_attack = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_special_attack.grid(row=400, column=200, padx=(5,10), sticky=W)
    
    lbl_special_defense = ttk.Label(frm_stats, text='Special Defense:')
    lbl_special_defense.grid(row=500, column=100, padx=(10,0), pady=10, sticky=E)
    prg_special_defense = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_special_defense.grid(row=500, column=200, padx=(5,10), sticky=W)
    
    lbl_speed = ttk.Label(frm_stats, text='Speed:')
    lbl_speed.grid(row=600, column=100, padx=(10,0), pady=10, sticky=E)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_speed.grid(row=600, column=200, padx=(5,10), sticky=W)

    
    root.mainloop()
    
main()
