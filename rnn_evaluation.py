import matplotlib.pyplot as plt
import pickle
def rnn_graph(userInput,timeArr):
    plt.subplots_adjust(wspace=0.2,hspace=0.2)
    for ix,cname in enumerate(userInput):
        for iix,ctime in enumerate(timeArr):
            plt.subplot(len(userInput),len(timeArr),ix+iix+1)
            with open(r"models\{}_{}_fit_his".format(cname,ctime),"rb") as fp:
                fit_his =pickle.load(fp)
                plt.subplot(1, 2, 2)
                plt.plot(fit_his.history["loss"],label="train loss")
                plt.plot(fit_his.history["val_acc"],label = "valid loss")
                plt.legend()
                plt.title(f"{cname}_{ctime}MAE LOSS")
    plt.show()
def convertValue(scaler,val):
    return scaler.inverse_transform(val)
def today_predict(rmodel,today_x):
    return rmodel.predict(today_x)
def evaluationModel(rmodel,xd,yd):
    return rmodel.evaluate(xd,yd)

