import { defineRecipe } from "@chakra-ui/react"

export const buttonRecipe = defineRecipe({
  base: {
    fontWeight: "bold",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    colorPalette: "brand",
    // bg:"button.bg",
    // color:"button.text",
    // _hover:{
    //   bg:"button.bg",
    //   color:"button.text",
    // },
    // _active:{
    //   bg:"button.bg",
    //   color:"button.text",
    // }
  },
  variants: {
    variant: {
      ghost: {
        bg: "transparent",
        _hover: {
          bg: "gray.100",
        },
      },
    },
  },
})
