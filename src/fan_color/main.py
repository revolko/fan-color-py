import colors
import temperatures


def main():
    avg_temp = temperatures.get_avg_temperature()

    with colors.ColorManager() as color_mng:  # repeat connection (OpenRGB SDK server is supposed to be unreliable)
        color_mng.set_color(avg_temp)


if __name__ == "__main__":
    main()
