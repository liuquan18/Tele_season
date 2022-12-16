#%%
import src.quick_plot.sptial_profile_generator as quick_plot
# %%
# independent all pattern
ind_all = quick_plot.first10_last10_index("ind","all")
ind_all.plot_all()
ind_all.create_doc()

#%%
# dependent all pattern
ind_all = quick_plot.first10_last10_index("dep","all")
ind_all.plot_all()
ind_all.create_doc()

# %%
# independent first pattern
ind_all = quick_plot.first10_last10_index("ind","first")
ind_all.plot_all()
ind_all.create_doc()

# %%
# dependent first pattern
ind_all = quick_plot.first10_last10_index("dep","first")
ind_all.plot_all()
ind_all.create_doc()
# %%
