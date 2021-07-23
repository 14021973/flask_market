USE [_TEST_ŚMIECI]
GO
/****** Object:  Table [dbo].[KZitem]    Script Date: 09.07.2021 14:58:41 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KZitem](
	[Id] [int] NOT NULL,
	[name] [nvarchar](55) NOT NULL,
	[price] [int] NOT NULL,
	[barcode] [nvarchar](12) NOT NULL,
	[description] [nvarchar](255) NOT NULL,
	[owner] [int] NOT NULL,
 CONSTRAINT [PK_item] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[KZuser]    Script Date: 09.07.2021 14:58:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KZuser](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[username] [nvarchar](55) NOT NULL,
	[email_address] [nvarchar](55) NOT NULL,
	[password_hash] [nvarchar](100) NOT NULL,
	[budget] [int] NOT NULL,
 CONSTRAINT [PK_KZuser] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[KZitem] ([Id], [name], [price], [barcode], [description], [owner]) VALUES (1, N'Towar_1', 500, N'123456789', N'Blahahahahaha', 1)
INSERT [dbo].[KZitem] ([Id], [name], [price], [barcode], [description], [owner]) VALUES (2, N'Towar_2', 499, N'812738912739', N'Hahahahahahh', 1)
GO
SET IDENTITY_INSERT [dbo].[KZuser] ON 

INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (1, N'user_1', N'user_1@email.com', N'asd878a9s7d98a', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (2, N'user_2', N'user_2@email.com', N'812738912739', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (3, N'12', N'12', N'', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (4, N'123', N'123', N'123', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (5, N'qwe', N'qwe', N'qwe', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (6, N'1234', N'1234', N'123', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (7, N'asd', N'asd@a.a', N'123123', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (8, N'12345', N'123@a.a', N'123456', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (9, N'kzaw', N'kzaw@kzaw.pl', N'$2b$12$jchJTPKLu1PAM1i1juO4luH0tGBYnE220sbfeRMDvX42sLYQcPyUa', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (10, N'kzaw1', N'kzaw1@wp.pl', N'$2b$12$dnCqCMSKtgbqS79iLOIzrOhJruqdkD6/e6bG1ADQYNMHERPO2Luoq', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (11, N'kzaw2', N'kzaw2@wp.pl', N'$2b$12$9C9w2q7nesaMV43LHirxB.892yzXaPdtKNiWk5T3e4swjxAeDaU1K', 1000)
INSERT [dbo].[KZuser] ([Id], [username], [email_address], [password_hash], [budget]) VALUES (12, N'kzaw3', N'kzaw3@wp.pl', N'$2b$12$IilqB2uVWpGy2cOKAaQFGe3VqoMz38I7vu5Zj9.s3WwlYwUr66gD2', 1000)
SET IDENTITY_INSERT [dbo].[KZuser] OFF
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [email_unq]    Script Date: 09.07.2021 14:58:42 ******/
ALTER TABLE [dbo].[KZuser] ADD  CONSTRAINT [email_unq] UNIQUE NONCLUSTERED 
(
	[email_address] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [username_unq]    Script Date: 09.07.2021 14:58:42 ******/
ALTER TABLE [dbo].[KZuser] ADD  CONSTRAINT [username_unq] UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
