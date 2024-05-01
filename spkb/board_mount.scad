



union() {
	color(alpha = 1.0, c = [0.2, 0.2, 0.2]) {
		difference() {
			union() {
				translate(v = [0, -54.2, 0]) {
					union() {
						translate(v = [-8.5, 0, 0]) {
							difference() {
								cylinder($fn = 16, center = false, h = 5, r = 3.058773474624955);
								translate(v = [0, 0, -0.05]) {
									cylinder($fn = 16, center = false, h = 5.1, r = 1.0195911582083184);
								}
							}
						}
						translate(v = [8.5, 0, 0]) {
							difference() {
								cylinder($fn = 16, center = false, h = 5, r = 3.058773474624955);
								translate(v = [0, 0, -0.05]) {
									cylinder($fn = 16, center = false, h = 5.1, r = 1.0195911582083184);
								}
							}
						}
					}
				}
				difference() {
					union() {
						translate(v = [-7.0, 0, 0]) {
							translate(v = [0, 1, 0]) {
								translate(v = [0, 0, 4.82]) {
									cube(center = true, size = [4, 4, 9.64]);
								}
							}
						}
						translate(v = [7.0, 0, 0]) {
							translate(v = [0, 1, 0]) {
								translate(v = [0, 0, 4.82]) {
									cube(center = true, size = [4, 4, 9.64]);
								}
							}
						}
					}
					union() {
						translate(v = [0, 0, 5.82]) {
							translate(v = [0, -26.5, 0]) {
								cube(center = true, size = [20.66, 53, 1.64]);
							}
						}
						translate(v = [0, 0, 3.75]) {
							union() {
								translate(v = [0, 2, 0]) {
									rotate(a = [90, 0, 0]) {
										hull() {
											translate(v = [-2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
											}
											translate(v = [2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
											}
										}
									}
								}
								translate(v = [0, 22, 0]) {
									rotate(a = [90, 0, 0]) {
										hull() {
											translate(v = [-2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
											}
											translate(v = [2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
											}
										}
									}
								}
							}
						}
					}
				}
			}
			union() {
				translate(v = [0, 0, 5.82]) {
					translate(v = [0, -26.5, 0]) {
						cube(center = true, size = [20.66, 53, 1.64]);
					}
				}
				translate(v = [0, 0, 3.75]) {
					union() {
						translate(v = [0, 2, 0]) {
							rotate(a = [90, 0, 0]) {
								hull() {
									translate(v = [-2.75, 0, 0]) {
										cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
									}
									translate(v = [2.75, 0, 0]) {
										cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
									}
								}
							}
						}
						translate(v = [0, 22, 0]) {
							rotate(a = [90, 0, 0]) {
								hull() {
									translate(v = [-2.75, 0, 0]) {
										cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
									}
									translate(v = [2.75, 0, 0]) {
										cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
									}
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, 0, 20]) {
		union() {
			color(alpha = 1.0, c = [0.2, 0.2, 0.2]) {
				difference() {
					union() {
						translate(v = [0, -54.2, 0]) {
							union() {
								translate(v = [-8.5, 0, 0]) {
									difference() {
										cylinder($fn = 16, center = false, h = 5, r = 3.058773474624955);
										translate(v = [0, 0, -0.05]) {
											cylinder($fn = 16, center = false, h = 5.1, r = 1.0195911582083184);
										}
									}
								}
								translate(v = [8.5, 0, 0]) {
									difference() {
										cylinder($fn = 16, center = false, h = 5, r = 3.058773474624955);
										translate(v = [0, 0, -0.05]) {
											cylinder($fn = 16, center = false, h = 5.1, r = 1.0195911582083184);
										}
									}
								}
							}
						}
						difference() {
							union() {
								translate(v = [-7.0, 0, 0]) {
									translate(v = [0, 1, 0]) {
										translate(v = [0, 0, 4.82]) {
											cube(center = true, size = [4, 4, 9.64]);
										}
									}
								}
								translate(v = [7.0, 0, 0]) {
									translate(v = [0, 1, 0]) {
										translate(v = [0, 0, 4.82]) {
											cube(center = true, size = [4, 4, 9.64]);
										}
									}
								}
							}
							union() {
								translate(v = [0, 0, 5.82]) {
									translate(v = [0, -26.5, 0]) {
										cube(center = true, size = [20.66, 53, 1.64]);
									}
								}
								translate(v = [0, 0, 3.75]) {
									union() {
										translate(v = [0, 2, 0]) {
											rotate(a = [90, 0, 0]) {
												hull() {
													translate(v = [-2.75, 0, 0]) {
														cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
													}
													translate(v = [2.75, 0, 0]) {
														cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
													}
												}
											}
										}
										translate(v = [0, 22, 0]) {
											rotate(a = [90, 0, 0]) {
												hull() {
													translate(v = [-2.75, 0, 0]) {
														cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
													}
													translate(v = [2.75, 0, 0]) {
														cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
													}
												}
											}
										}
									}
								}
							}
						}
					}
					union() {
						translate(v = [0, 0, 5.82]) {
							translate(v = [0, -26.5, 0]) {
								cube(center = true, size = [20.66, 53, 1.64]);
							}
						}
						translate(v = [0, 0, 3.75]) {
							union() {
								translate(v = [0, 2, 0]) {
									rotate(a = [90, 0, 0]) {
										hull() {
											translate(v = [-2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
											}
											translate(v = [2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
											}
										}
									}
								}
								translate(v = [0, 22, 0]) {
									rotate(a = [90, 0, 0]) {
										hull() {
											translate(v = [-2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
											}
											translate(v = [2.75, 0, 0]) {
												cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
											}
										}
									}
								}
							}
						}
					}
				}
			}
			color(alpha = 1.0, c = [0.0, 0.4, 0.0]) {
				union() {
					translate(v = [0, 0, 5.82]) {
						translate(v = [0, -26.5, 0]) {
							cube(center = true, size = [20.66, 53, 1.64]);
						}
					}
					translate(v = [0, 0, 3.75]) {
						union() {
							translate(v = [0, 2, 0]) {
								rotate(a = [90, 0, 0]) {
									hull() {
										translate(v = [-2.75, 0, 0]) {
											cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
										}
										translate(v = [2.75, 0, 0]) {
											cylinder($fn = 16, center = false, h = 6, r = 1.274488947760398);
										}
									}
								}
							}
							translate(v = [0, 22, 0]) {
								rotate(a = [90, 0, 0]) {
									hull() {
										translate(v = [-2.75, 0, 0]) {
											cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
										}
										translate(v = [2.75, 0, 0]) {
											cylinder($fn = 16, center = false, h = 20, r = 4.333262422385353);
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
